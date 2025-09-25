import random
from collections import deque
from netaddr import IPAddress
from typing import Tuple, Optional, Dict, Any

from cyst.api.environment.message import Message, Request, StatusOrigin, StatusValue, Status, ComponentState
from cyst.api.environment.messaging import EnvironmentMessaging
from cyst.api.environment.resources import EnvironmentResources
from cyst.api.host.service import ActiveServiceDescription, ActiveService


class DelayDefender(ActiveService):
    def __init__(self, msg: EnvironmentMessaging, res: EnvironmentResources, id:str, args: Optional[Dict[str, Any]]):
        self._msg = msg
        self._res = res
        self._id = id
        self._args = args

        self._time_window = args.get("message_threshold", 20)

        if "message_threshold" in args:
            delta = args.get("message_threshold_delta", 20)
            threshold = args["message_threshold"]
            self._message_threshold = random.randint(threshold - delta, threshold + delta)
        else:
            self._message_threshold = random.randint(50, 100)

        if "block_duration" in args:
            delta = args.get("block_duration_delta", 10)
            duration = args["block_duration"]
            self._block_duration = random.randint(duration - delta, duration + delta)
        else:
            self._block_duration = random.randint(20, 40)

        self._messages: Dict[IPAddress, deque] = {}
        self._blocks: Dict[IPAddress, float] = {}

    async def run(self) -> None:
        pass

    async def process_message(self, message: Message) -> Tuple[bool, int]:
        if not isinstance(message, Request):
            return True, 0

        time = self._res.clock.current_time()

        # If the address was blocked
        if message.src_ip in self._blocks:
            # we first check if the block has expired
            block_timeout = self._blocks[message.src_ip]
            # if so, we remove the block and move along
            if block_timeout < time:
                del self._blocks[message.src_ip]
                unblock_signal = self._msg.create_signal(message.platform_specific["caller_id"],
                                                         ComponentState.UNBLOCKED,
                                                         self._id, message.id,
                                                         f"Unblocking of an IP {str(message.src_ip)} due to timeout expiration")
                self._msg.send_message(unblock_signal)
            # otherwise, we reinstate the block
            else:
                self._blocks[message.src_ip] = time + self._block_duration
                # and notify the poor agent
                response = self._msg.create_response(message, Status(StatusOrigin.NETWORK, StatusValue.ERROR),
                                                     "Too many requests.", message.session, message.auth)
                self._msg.send_message(response)

                block_signal = self._msg.create_signal(message.platform_specific["caller_id"],
                                                       ComponentState.BLOCKED | ComponentState.REPEATED_OCCURRENCE,
                                                       self._id, message.id,
                                                       f"Blocking of an IP {str(message.src_ip)} due to excessive number of messages. Duration: {self._block_duration} s.")
                self._msg.send_message(block_signal)
                return False, 0

        queue = self._messages.get(message.src_ip, None)
        if not queue:
            queue = deque()
            self._messages[message.src_ip] = queue

        # Purge older messages
        while len(queue) != 0:
            entry_time = queue[0]
            if time - entry_time > self._time_window:
                queue.popleft()
            else:
                break

        queue.append(time)

        if len(queue) >= self._message_threshold:
            # When crossing a message threshold, we send an error response ...
            response = self._msg.create_response(message, Status(StatusOrigin.NETWORK, StatusValue.ERROR),
                                                 "Too many requests.", message.session, message.auth)
            self._msg.send_message(response)
            # ... add the IP to the blocklist ...
            self._blocks[message.src_ip] = time + self._block_duration
            # ... and signal the environment that there was a blocking
            block_signal = self._msg.create_signal(message.platform_specific["caller_id"],
                                                   ComponentState.BLOCKED | ComponentState.FIRST_OCCURRENCE,
                                                   self._id, message.id,
                                                   f"Blocking of an IP {str(message.src_ip)} due to excessive number of messages. Duration: {self._block_duration} s.")
            self._msg.send_message(block_signal)
            return False, 0
        else:
            return True, 0

def create_defender(msg: EnvironmentMessaging, res: EnvironmentResources, id:str, args: Optional[Dict[str, Any]]) -> ActiveService:
    defender = DelayDefender(msg, res, id, args)
    return defender


service_description = ActiveServiceDescription(
    name="aica-challenge-1-delay-defender",
    description="A simple defender that causes delays after excessive number of messages observed.",
    creation_fn=create_defender
)
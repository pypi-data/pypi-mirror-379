###
# Minimal example of publishing events to the IronFlock Platform.
###

import asyncio
from datetime import datetime
from ironflock import IronFlock

# create a ironflock instance, which auto connects to the IronFlock Platform
# the ironflock instance handles authentication and reconnects when connection is lost
rw = IronFlock()


async def main():
    while True:
        # publish an event (if connection is not established the publish is skipped)
        publication = await rw.publish_to_table(
            "sensordata",
            dict(temperature=25, tsp=datetime.now().astimezone().isoformat()),
        )
        print(publication)
        await asyncio.sleep(3)


if __name__ == "__main__":
    # run the main coroutine
    asyncio.get_event_loop().create_task(main())
    # run the ironflock component
    rw.run()

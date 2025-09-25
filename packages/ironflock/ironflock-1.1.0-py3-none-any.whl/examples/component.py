###
# Minimal example of creating an Autobahn asyncio Component
# for connecting to the IronFlock Platform.
# Compared to the IronFlock() class, the Component approach allows
# more control, e.g. reacting to the lifecycle of the component:
# you can register callback functions like on_join or on_leave.
# For more details checkout:
# https://autobahn.readthedocs.io/en/latest/wamp/programming.html#application-components
###

from asyncio import sleep
from autobahn.asyncio.component import run
from autobahn.wamp.interfaces import ISession
from ironflock import create_application_component

# returns an Autobahn asyncio Component, for more information checkout:
# https://autobahn.readthedocs.io/en/latest/reference/autobahn.asyncio.html
comp = create_application_component()


@comp.on_join
async def onJoin(session: ISession, details):
    print("joined router")
    print(session, details)

    def handler(*args, **kwargs):
        print("got event")
        print(args, kwargs)

    # subscribe to a topic
    session.subscribe(handler, "test.publish.com")

    # publish an event every second
    while True:
        session.publish("test.publish.com", 1, "two", 3, foo="bar")
        await sleep(1)


if __name__ == "__main__":
    run([comp])

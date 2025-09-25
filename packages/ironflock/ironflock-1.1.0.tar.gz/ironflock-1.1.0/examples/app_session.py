###
# Minimal example of creating an Autobahn asyncio ApplicationSession
# for connecting to the IronFlock Platform.
# Compared to the IronFlock() class, the ApplicationSession approach allows
# more control reacting to the lifecycle of the Session:
# you can register callback functions like on_join or on_leave.
# For more details checkout:
# https://autobahn.readthedocs.io/en/latest/wamp/programming.html#application-components
###

from asyncio import sleep
from autobahn.wamp.interfaces import ISession
from ironflock import create_application_session

# returns an Autobahn asyncio ApplicationSession and ApplicationRunner, for more information checkout:
# https://autobahn.readthedocs.io/en/latest/reference/autobahn.asyncio.html
AppSession, runner = create_application_session()


class Application(AppSession):
    async def onJoin(session: ISession, details):
        print("joined router")
        print(session, details)

        # publish an event every second
        while True:
            session.publish("test.publish.com", 1, "two", 3, foo="bar")
            await sleep(1)


if __name__ == "__main__":
    runner.run(Application)

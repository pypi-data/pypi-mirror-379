from asyncio.events import get_event_loop
from ironflock import IronFlock

async def main():
    rw = IronFlock(serial_number="7652ee0b-c2cb-466a-b8ee-fec4167bf7ce")
    result = await rw.publish('re.meetup.data', {"temperature": 20})
    print(result)

if __name__ == "__main__":
    get_event_loop().run_until_complete(main())
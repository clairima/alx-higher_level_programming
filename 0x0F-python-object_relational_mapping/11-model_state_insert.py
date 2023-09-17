#!/usr/bin/python3
"""
adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.schema import Table
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print("{}".format(new_state.id))
    session.close()

import sqlite3
from sqlite3 import Error

create_history = """ CREATE TABLE IF NOT EXISTS history (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        round_one text,
                                        round_two text,
                                        round_three text,
                                        date_played text
                                    ); """
                                    
create_topTen = """CREATE TABLE IF NOT EXISTS Top_10(
                                    id integer PRIMARY KEY,
                                    player_name text NOT NULL,
                                    round_one text,
                                    round_two text,
                                    round_three text,
                                    date_played text,
                                    FOREIGN KEY (player_name) REFERENCES history (name)
                                );"""

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn
            
def create_table(conn, create_table):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)
        
def add_player(conn, player_info):
    """
    Add a player into the history table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO history(name, round_one, round_two, round_three, date_played)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, player_info)
    conn.commit()
    return cur.lastrowid

def addToHistory(conn, player_info):
    
    if conn is not None: #if connected
        
        add_player(conn, player_info)

    else:
        print("Error! cannot add row to the database due to connection.")
        
def addToTop10(conn, player_info):
    """
    Add a player into the history table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Top_10(player_name, round_one, round_two, round_three, date_played)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, player_info)
    conn.commit()
    return cur.lastrowid

def addPlayerToTT(conn, player_info):
    
    if conn is not None: #if connected
        
        addToTop10(conn, player_info)

    else:
        print("Error! cannot add row to the database due to connection.")
        
def createDatabase(conn):
    # create history table
    create_table(conn, create_history)
    # create top ten table
    create_table(conn, create_topTen)
    
def checkRows(conn):
    cur = conn.cursor()
    cur.execute('select * from Top_10')
    rows = len(cur.fetchall())
    return rows
    
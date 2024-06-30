def insert_alarm(db_conn, data):
    """
    Insert an alarm into the database if an alarm with the same node_id and alarm_value does not already exist.

    Args:
        db_conn: The database connection.
        data (dict): The alarm data to insert.

    Returns:
        dict or str: The inserted alarm data or a message indicating the alarm already exists.
    """
    # Check if an alarm with the same node_id and alarm_value already exists
    db_conn.cur.execute(
        """
        SELECT 1 FROM alarms
        WHERE node_id = %s AND alarm_value = %s AND alarm_status = TRUE;
        """,
        (data["node_id"], data["alarm_value"])
    )
    if db_conn.cur.fetchone():
        return "Alarm with the same node_id and alarm_value already exists."

    # If no existing alarm is found, insert the new alarm
    db_conn.cur.execute(
        """
        INSERT INTO alarms (node_id, alarm_type, alarm_value)
        VALUES (%s, %s, %s)
        RETURNING id, timestamp, node_id, alarm_type, alarm_value;
        """,
        (data["node_id"], data["alarm_type"], data["alarm_value"])
    )
    db_conn.conn.commit()
    alarm = db_conn.cur.fetchone()
    return alarm

def read_alarms(db_conn):
    """
    Get all alarms from the database.

    Args:
        db_conn: The database connection.

    Returns:
        list: The list of alarms.
    """
    db_conn.cur.execute(
            """
            SELECT id, timestamp, node_id, alarm_type, alarm_value
            FROM alarms
            WHERE alarm_status = TRUE;
            """
        )
    alarms = db_conn.cur.fetchall()
    return alarms

def update_alarm(db_conn, id, data):
    """
    Update the alarm as read in the database.

    Args:
        db_conn: The database connection.
        id (str): The ID of the alarm to update.

    Returns:
        dict: The updated alarm data.
    """
    remarks = data.get("remarks", None)
    db_conn.cur.execute(
            """
            UPDATE alarms
            SET alarm_status = FALSE,
                resolved_remarks = %s
            WHERE id = %s
            RETURNING id, timestamp, node_id, alarm_type, alarm_value, alarm_status,resolved_remarks;
            """,
            (remarks, id)
        )
    db_conn.conn.commit()
    alarm = db_conn.cur.fetchone()
    return alarm
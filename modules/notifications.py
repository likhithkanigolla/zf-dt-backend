def insert_notification(db_conn, data):
    """
    Insert a notification into the database.

    Args:
        db_conn: The database connection.
        data (dict): The notification data to insert.

    Returns:
        dict: The inserted notification data.
    """
    db_conn.cur.execute(
            """
            INSERT INTO notifications (node_id, notification_type, notification_value)
            VALUES (%s, %s, %s)
            RETURNING id, timestamp, node_id, notification_type, notification_value;
            """,
            (data["node_id"], data["notification_type"], data["notification_value"])
        )
    db_conn.conn.commit()
    notification = db_conn.cur.fetchone()
    return notification

def update_notification(db_conn, id):
    """
    Update the notification as read in the database.

    Args:
        db_conn: The database connection.
        id (str): The ID of the notification to update.

    Returns:
        dict: The updated notification data.
    """
    db_conn.cur.execute(
            """
            UPDATE notifications
            SET read_status = TRUE
            WHERE id = %s
            RETURNING id, timestamp, node_id, notification_type, notification_value, read_status;
            """,
            (id,)
        )
    db_conn.conn.commit()
    notification = db_conn.cur.fetchone()
    return notification

def read_notifications(db_conn):
    """
    Get all notifications from the database.

    Args:
        db_conn: The database connection.

    Returns:
        list: The list of notifications.
    """
    db_conn.cur.execute(
            """
            SELECT id, timestamp, node_id, notification_type, notification_value, read_status
            FROM notifications
            WHERE read_status = FALSE 
            ORDER BY timestamp DESC;
            """
        )
    notifications = db_conn.cur.fetchall()
    return notifications

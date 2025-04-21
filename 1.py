def delete_user_by_name(name):
    cur.execute("SELECT id FROM users WHERE username = %s", (name,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        cur.execute("DELETE FROM user_scores WHERE user_id = %s", (user_id,))
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        print(f"User '{name}' and all their scores have been deleted.")
    else:
        print(f"User '{name}' not found.")



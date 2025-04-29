import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.execute("""
                CALL inc_semestre(1);
                """)
        
        print("Procedimento 'inc_semestre' executado para o semestre 1.")

        conn.commit()
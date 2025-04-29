import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.execute("""
                UPDATE turma
                SET estado = 'Fechado'
                WHERE codigo = 'CC2024DS1'
                """)
        
        cur.execute("""
                DELETE FROM Aluno_Turma
                WHERE turma_id = (SELECT id FROM turma WHERE codigo = 'CC2024DS1')
                """)
        
        conn.commit()
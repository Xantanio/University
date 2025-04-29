CREATE OR REPLACE PROCEDURE inc_semestre(p_semestre INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Aluno
    SET semestre = semestre + 1
    WHERE semestre = p_semestre;

    RAISE NOTICE 'Semestre dos alunos no semestre % incrementado para %', p_semestre, p_semestre + 1;
END;
$$;

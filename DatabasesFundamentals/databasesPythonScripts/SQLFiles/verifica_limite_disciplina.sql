CREATE OR REPLACE FUNCTION verifica_limite_disciplinas()
RETURNS TRIGGER AS $$
BEGIN
    IF (
        SELECT COUNT(*)
        FROM Aluno_Turma
        WHERE aluno_id = NEW.aluno_id
          AND turma_id IN (
              SELECT id 
              FROM Turma 
              WHERE semestre = (SELECT semestre FROM Turma WHERE id = NEW.turma_id LIMIT 1)
          )
    ) >= 3 THEN
        RAISE EXCEPTION 'O aluno já está matriculado no número máximo de disciplinas para este semestre!';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Creates a store procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
	IN user_id INTEGER
	)
	BEGIN
		DECLARE average_weighted_score FLOAT;

		SELECT SUM(cors.score * pjs.weight) / SUM(pjs.weight) INTO average_weighted_score
		FROM projects AS pjs
		JOIN corrections AS cors
		ON pjs.id = cors.project_id
		AND cors.user_id = user_id;

		UPDATE users
		SET average_score = average_weighted_score
		WHERE users.id = user_id;
	END$$

DELIMITER ;

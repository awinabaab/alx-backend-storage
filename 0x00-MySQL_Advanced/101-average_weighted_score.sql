-- Creates a store procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all student

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
	BEGIN
		UPDATE users
		JOIN (
			SELECT
				cors.user_id,
				SUM(cors.score * pjs.weight) / SUM(pjs.weight) AS average_weighted_score
				FROM projects AS pjs
				JOIN corrections AS cors
				ON pjs.id = cors.project_id
				GROUP BY cors.user_id
		)
		AS average_weighted_scores
		ON users.id = average_weighted_scores.user_id
		SET users.average_score = average_weighted_scores.average_weighted_score;
	END$$

DELIMITER ;

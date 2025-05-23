-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student

DELIMITER :

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)
	BEGIN
		DECLARE av_score FLOAT;

		SELECT SUM(score) / COUNT(*) AS score INTO av_score
		FROM corrections
		WHERE corrections.user_id = user_id;

		UPDATE users
		SET average_score = av_score
		WHERE id = user_id;
	END:

DELIMITER ;

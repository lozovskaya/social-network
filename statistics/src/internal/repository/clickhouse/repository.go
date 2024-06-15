package clickhouse

import (
	"context"
	"database/sql"
	"grpc-stats/internal/domain"
)


type Repository struct {
    db  *sql.DB
}

func New(db  *sql.DB) *Repository {
	return &Repository{db: db}
}

func (r *Repository) GetPostStats(ctx context.Context, postID int32) (domain.PostStats, error) {
	var numLikes int32
	var err = r.db.QueryRow(`
		SELECT countDistinct(user_id)
		FROM post_likes
		WHERE post_id = $1
		GROUP BY post_id
	`, postID).Scan(&numLikes)
	if err == sql.ErrNoRows {
		numLikes = 0
	} else if err != nil {
		return domain.PostStats{}, err
	}

	var numViews int32
	err = r.db.QueryRow(`
		SELECT countDistinct(user_id)
		FROM post_views
		WHERE post_id = $1
		GROUP BY post_id
	`, postID).Scan(&numViews)
	if err == sql.ErrNoRows {
		numViews = 0
	} else if err != nil {
		return domain.PostStats{}, err
	}
	
	return domain.PostStats {
		Likes:numLikes,
		Views:numViews,
	}, nil
}


func (r *Repository) GetPopularPosts(ctx context.Context, actionType string, size int32) (*[]domain.PostStatsByOneParameter, error) {
	var table_name string;
	if actionType == "like" {
		table_name = "post_likes"
	} else {
		table_name = "post_views"
	}
	rows, err := r.db.Query(`
					SELECT post_owner, post_id, countDistinct(user_id) as count
					FROM $1
					GROUP BY post_id, post_owner
					ORDER BY count DESC
					LIMIT $2`, table_name, size)
	if err != nil {
		return nil, err
	}

	var posts []domain.PostStatsByOneParameter
	for rows.Next() {
		var post_owner, postID, count int32
		if err := rows.Scan(&post_owner, &postID, &count); err != nil {
			return nil, err
		}
		posts = append(posts, domain.PostStatsByOneParameter{
			PostOwner: post_owner,
			PostID:   postID,
			Count:    count,
		})
	}

	return &posts, nil
}


func (r *Repository) GetPopularUsers(ctx context.Context, count int32) (*[]domain.UserInfoLikes, error) {
	rows, err := r.db.Query(`
		SELECT post_owner, countDistinct(user_id, post_id) as total_likes
		FROM post_likes
		GROUP BY post_owner
		ORDER BY total_likes DESC
		LIMIT $1
	`, count)
	if err != nil {
		return nil, err
	}

	var users []domain.UserInfoLikes
	for rows.Next() {
		var userID, likes int32
		if err := rows.Scan(&userID, &likes); err != nil {
			return nil, err
		}
		users = append(users, domain.UserInfoLikes{
			UserID:   userID,
			Likes: likes,
		})
	}

	return &users, nil
}
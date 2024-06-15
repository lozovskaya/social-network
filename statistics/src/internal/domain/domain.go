package domain

import (
	"context"
)

type (
	StatsRepository interface {
		GetPostStats(ctx context.Context, postID int32) (PostStats, error)
		GetPopularPosts(ctx context.Context, actionType string, size int32) (*[]PostStatsByOneParameter, error)
		GetPopularUsers(ctx context.Context, count int32) (*[]UserInfoLikes, error)
	}
)

type Model struct {
	Repository StatsRepository
}

func NewModel(repository StatsRepository) *Model {
	return &Model{Repository: repository}
}

type (
	PostStats struct {
		Likes int32  `json:"likes"`
		Views int32 `json:"views"`
	}

	PostStatsByOneParameter struct {
		PostOwner int32  `json:"post_owner"`
		PostID int32  `json:"post_id"`
		Count int32 `json:"count"`
	}

	UserInfoLikes struct {
		UserID int32  `json:"user_id"`
		Likes int32   `json:"likes"`
	}
)

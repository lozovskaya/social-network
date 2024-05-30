package domain

import (
	"context"
	"time"
)

type (
	PostsRepository interface {
		CreatePost(ctx context.Context, userID int32, post PostCreate) (int32, error)
		UpdatePost(ctx context.Context, userID int32, updatedPost PostUpdate) error
		DeletePost(ctx context.Context, userID int32, postID int32) error
		GetPostById(ctx context.Context, postID int32) (*Post, error)
		ListPosts(ctx context.Context, pageNum int32, pageSize int32) (*[]Post, error)
	}
)

type Model struct {
	Repository PostsRepository
}

func NewModel(repository PostsRepository) *Model {
	return &Model{Repository: repository}
}

type (
	PostCreate struct {
		Title string  `json:"title"`
		Content string `json:"content"`
	}

	PostUpdate struct {
		Id int32 `json:"post_id"`
		Title string  `json:"title"`
		Content string `json:"content"`
	}

	Post struct {
		ID        int32    `json:"post_id"`
		UserID    int32    `json:"user_id"`
		Title     string    `json:"title"`
		Content   string    `json:"content"`
		CreatedAt time.Time `json:"created_at"`
		EditedAt  time.Time `json:"edited_at"`
	}
)

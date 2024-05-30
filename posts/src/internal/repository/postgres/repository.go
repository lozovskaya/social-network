package postgres

import (
	"context"
	"fmt"
	"grpc-posts-server/internal/domain"
	"grpc-posts-server/internal/repository/schema"
	"time"

	sq "github.com/Masterminds/squirrel"
	"github.com/jackc/pgx/v4/pgxpool"
)

var psql = sq.StatementBuilder.PlaceholderFormat(sq.Dollar)

type Repository struct {
    db *pgxpool.Pool
}

func New(db *pgxpool.Pool) *Repository {
	return &Repository{db: db}
}

var (
	postsTableColumns = []string{"user_id", "title", "content", "created_at", "edited_at"}
	postsTableColumnsWithPostId = []string{"post_id", "user_id", "title", "content", "created_at", "edited_at"}

)

const (
	postsTable = "posts"
)

func (r *Repository) CreatePost(ctx context.Context, userID int32, post domain.PostCreate) (int32, error) {
	query := psql.Insert(postsTable).Columns(postsTableColumns...).
									 Values(userID, post.Title, post.Content, time.Now(), time.Now()).Columns().
									 Suffix("RETURNING post_id")
	raw_sql, args, err := query.ToSql()
	if err != nil {
		return 0, fmt.Errorf("building SQL create post: %w", err)
	}
	var postid int32
	err = r.db.QueryRow(ctx, raw_sql, args...).Scan(&postid)
	if err != nil {
		return 0, fmt.Errorf("execute creating post: %w", err)
	}
	return postid, nil
}

func (r *Repository) UpdatePost(ctx context.Context, userID int32, updatedPost domain.PostUpdate) error {
	query := psql.Update(postsTable).
					Set("title", updatedPost.Title).
					Set("content", updatedPost.Content).
					Set("edited_at", time.Now()).
					Where(sq.Eq{"post_id": updatedPost.Id, "user_id": userID})
	raw_sql, args, err := query.ToSql()
	if err != nil {
		return fmt.Errorf("building SQL updating post: %w", err)
	}
	_, err = r.db.Exec(ctx, raw_sql, args...)
    if err != nil {
        return fmt.Errorf("execute updating post: %w", err)
    }
    return nil
}

func (r *Repository) DeletePost(ctx context.Context, userID int32, postID int32) error {	
	query := psql.Delete(postsTable).
						Where(sq.Eq{"post_id": postID, "user_id": userID})			
	raw_sql, args, err := query.ToSql()
	if err != nil {
		return fmt.Errorf("building SQL deleting post: %w", err)
	}
	_, err = r.db.Exec(ctx, raw_sql, args...)
	if err != nil {
		return fmt.Errorf("execute deleting post: %w", err)
	}
	return nil
}

func (r *Repository) GetPostById(ctx context.Context, postID int32) (*domain.Post, error) {
	query := psql.Select(postsTableColumnsWithPostId...).
								From(postsTable).
								Where(sq.Eq{"post_id": postID})
	raw_sql, args, err := query.ToSql()
	if err != nil {
		return nil, fmt.Errorf("building SQL deleting post: %w", err)
	}
	var result schema.Post
    err = r.db.QueryRow(ctx, raw_sql, args...).Scan(
        &result.ID, &result.UserID, &result.Title, &result.Content,
        &result.CreatedAt, &result.EditedAt)
    if err != nil {
        return nil, err
    }

	var postModel = bindPostToModel(result)
    return &postModel, nil
}


func (r *Repository) ListPosts(ctx context.Context, pageNum int32, pageSize int32) (*[]domain.Post, error) {
	offset := (pageNum - 1) * pageSize

    query := psql.Select(postsTableColumnsWithPostId...).
        From(postsTable).
        Offset(uint64(offset)).
        Limit(uint64(pageSize))

    raw_sql, args, err := query.ToSql()
    if err != nil {
        return nil, err
    }

    rows, err := r.db.Query(ctx, raw_sql, args...)
    if err != nil {
        return nil, err
    }
    defer rows.Close()

    var posts []domain.Post
    for rows.Next() {
        var post schema.Post
        err := rows.Scan(
            &post.ID, &post.UserID, &post.Title, &post.Content,
            &post.CreatedAt, &post.EditedAt,
        )
        if err != nil {
            return nil, err
        }
        posts = append(posts, bindPostToModel(post))
    }
    return &posts, nil
}

func bindPostToModel(data schema.Post) domain.Post {
	return domain.Post{ID: int32(data.ID), UserID: data.UserID, Title: data.Title, 
					Content: data.Content, CreatedAt: data.CreatedAt, EditedAt: data.EditedAt}
}
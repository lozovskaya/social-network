package schema

import "time"

type Post struct {
	ID        int32    `db:"post_id"`
	UserID    int32   `db:"user_id"`
	Title     string    `db:"title"`
	Content   string    `db:"content"`
	CreatedAt time.Time `db:"created_at"`
	EditedAt  time.Time `db:"edited_at"`
}


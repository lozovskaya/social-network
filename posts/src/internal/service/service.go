package post_service

import (
	"context"
	"fmt"
	pb "grpc-posts-server/api"
	"grpc-posts-server/internal/domain"

	"google.golang.org/protobuf/types/known/timestamppb"
)

type PostService struct {
    pb.UnimplementedPostServiceServer
	model *domain.Model
}

func New(model *domain.Model) *PostService {
	return &PostService{model: model}
}


func (s *PostService) CreatePost(ctx context.Context, req *pb.CreatePostRequest) (*pb.CreatePostResponse, error) {
    id, err := s.model.Repository.CreatePost(ctx, req.GetUserId(), domain.PostCreate{Title: req.GetTitle(), Content:   req.GetContent()})
    if err != nil {
        return nil, err
    }

    return &pb.CreatePostResponse{Id: id}, nil
}

func (s *PostService) UpdatePost(ctx context.Context, req *pb.UpdatePostRequest) (*pb.EmptyResponse, error) {
    err := s.model.Repository.UpdatePost(ctx, req.GetUserId(), domain.PostUpdate{Id: req.GetId(), Title: req.GetTitle(), Content: req.GetContent()})
    if err != nil {
        return nil, err
    }
    return &pb.EmptyResponse{}, nil
}

func (s *PostService) DeletePost(ctx context.Context, req *pb.DeletePostRequest) (*pb.EmptyResponse, error) {
    err := s.model.Repository.DeletePost(ctx, req.GetUserId(), req.GetId())
    if err != nil {
        return nil, err
    }
    return &pb.EmptyResponse{}, nil
}

func (s *PostService) GetPostById(ctx context.Context, req *pb.GetPostByIdRequest) (*pb.PostResponse, error) {
    post, err := s.model.Repository.GetPostById(ctx, req.GetId())
    if err != nil {
        return nil, err
    }
    if post == nil {
        return nil, fmt.Errorf("post with the given id doesn't exist")
    }

    return &pb.PostResponse{Post: convertToPbPost(*post)}, nil
}

func (s *PostService) ListPosts(ctx context.Context, req *pb.ListPostsRequest) (*pb.ListPostsResponse, error) {
    response, err := s.model.Repository.ListPosts(ctx, req.GetPage(), req.GetPageSize())
    if err != nil {
        return nil, err
    }
    posts := *response

    pbPosts := make([]*pb.Post, len(posts))
    for i, post := range posts {
        pbPosts[i] = convertToPbPost(post)
    }

    return &pb.ListPostsResponse{
        Posts:      pbPosts,
    }, nil
}

// Convertors

func convertToPbPost(post domain.Post) *pb.Post {
	return &pb.Post{
        Id:        post.ID,
        UserId:    post.UserID,
        Title:     post.Title,
        Content:   post.Content,
        CreatedAt: timestamppb.New(post.CreatedAt),
        EditedAt:  timestamppb.New(post.EditedAt),
    }
}

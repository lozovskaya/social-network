package stats_service

import (
	"context"
	pb "grpc-stats/api"
	"grpc-stats/internal/domain"
	"strconv"
)

type StatsService struct {
    pb.UnimplementedStatsServiceServer
	model *domain.Model
}

func New(model *domain.Model) *StatsService {
	return &StatsService{model: model}
}


func (s *StatsService) GetPostStats(ctx context.Context, req *pb.GetPostStatsRequest) (*pb.GetPostStatsResponse, error) {
    post_stats, err := s.model.Repository.GetPostStats(ctx, req.GetId())
    if err != nil {
        return nil, nil
    }

    return &pb.GetPostStatsResponse{Likes: post_stats.Likes, Views: post_stats.Views}, nil
}

func (s *StatsService) GetPopularPosts(ctx context.Context, req *pb.GetPopularPostsRequest) (*pb.GetPopularPostsResponse, error) {
    popular_posts, err := s.model.Repository.GetPopularPosts(ctx, req.GetActionType(), req.GetSize())
    if err != nil {
        return nil, nil
    }

    var pb_posts []*pb.PostStatsByOneParameter

    for _, post := range *popular_posts {
        var user_login = strconv.Itoa(int(post.PostOwner)) 
        pb_posts = append(pb_posts, &pb.PostStatsByOneParameter{Id: post.PostID, UserLogin: user_login, Count: post.Count})
    } 

    return &pb.GetPopularPostsResponse{Posts: pb_posts}, nil
}

func (s *StatsService) GetPopularUsers(ctx context.Context, req *pb.GetPopularUsersRequest) (*pb.GetPopularUsersResponse, error) {
    popular_users, err := s.model.Repository.GetPopularUsers(ctx, req.GetCount())
    if err != nil {
        return nil, nil
    }

    var pb_users []*pb.UserInfo

    for _, user := range *popular_users {
        var user_login = strconv.Itoa(int(user.UserID)) // todo: replace with real login
        pb_users = append(pb_users, &pb.UserInfo{Login: user_login, Likes: user.Likes})
    } 

    return &pb.GetPopularUsersResponse{Users: pb_users}, nil
}
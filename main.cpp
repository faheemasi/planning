#include <string>
#include <iostream>
#include <fstream>
#include <cmath>
#include <chrono>

// #include <cairomm/cairomm.h>
// #include <cairomm/context.h>
// #include <cairomm/surface.h>
// #include <cairomm/fontface.h>
#include "pbPlots.hpp"
#include "supportLib.hpp"

#include "graph.hpp"
#include "heuristics.hpp"

int main(int argc, char **argv)
{
    std::cout<<"Starting"<<std::endl;
    std::vector<Eigen::Vector2d> path;
    // reading the path file which contains the points
    std::ifstream pathFile;
    pathFile.open("path.txt");
    std::string rd_line;//line read from file
    int sp_1=0; //First space position
    int sp_2=0; //Second space position
    float value_x=0.0;// x value
    float value_y=0.0;// y value
    if(pathFile.is_open()){
        while(std::getline(pathFile,rd_line)){
            sp_1=rd_line.find(' '); // first space position
            sp_2=rd_line.find(' ',sp_1+1); // first space position
            
            std::cout<<rd_line<<'\n';
            if(rd_line.substr(sp_1+1,2)=="x:"){
                value_x=std::stof(rd_line.substr(sp_1+3,sp_2-sp_1-2));
                std::cout<<value_x<<'\n';
            }

            if(rd_line.substr(sp_2+1,2)=="y:"){
                value_y=std::stof(rd_line.substr(sp_2+3,rd_line.length()-sp_2));
                std::cout<<value_y<<'\n';
            }
            Eigen::Vector2d point_xy(value_x,value_y);
            path.push_back(point_xy);
        }
        
    }

    Mandoline::Graph path_polygon;
    Mandoline::Polygon(path).Compute(path_polygon);




// 		auto proto = tx_plan().initProto();
// 		auto goal_proto = tx_goal().initProto();
// 		//uncomment this for path traveled
// 		/*
// 		auto poses_proto = proto.initPoses((polygon1.Segments().size()-1)*2);
// 		std::vector<std::array<Eigen::Vector2d, 2>> segments = polygon1.Segments();
// 		*/
// 		//uncomment this for total plan
// 		double dist=100.0;
// 		double dist1=100.0;
// 		std::vector<std::array<Eigen::Vector2d, 2>> segments = polygon_slice.Segments();
// 		//std::vector<std::array<Eigen::Vector2d, 2>> segments = polygon_slice.SegmentsWithAdditionalWaypoints(0.3);



// 		std::vector<std::array<Eigen::Vector2d, 2>> segmentsLoopsRemoved = {};

// 		std::vector<std::array<Eigen::Vector2d, 2>> segmentsLoopsRemoved1 = {};

// 		for(size_t i = 0;i < segments.size(); i++)
// 		{
// 				Vector2d t1=segments[i][1];
// 				Vector2d t=segments[i][0];
				
// 				printf("Before (x0,y0),(x1,y1) - (%f,%f),  (%f,%f) \n",t[0],t[1],t1[0],t1[1]);

// 			if( i< segments.size() ) 
// 			{
// 					if(i<segments.size()-1) {
// 					dist = (segments[i][0]-segments[i+1][0]).norm();
// 					if (dist<eps) 
// 					{
// 						loop=1;
// 						Vector2d tmp=segments[i][0];
// 						Vector2d tmp1=segments[i][0];
// 						tmp1[0]=tmp[0];
// 						tmp1[1]=tmp[1]-0.005;
// 						segments[i][0]=tmp;
// 						segments[i][1]=tmp1;

						

// 						segmentsLoopsRemoved.push_back(segments[i]);

// 					} 
// 					else 
// 					{
// 						loop=0;
// 						Vector2d tmp=segments[i][0];
// 						tmp[0]=tmp[0]-(float) rand()/RAND_MAX*0.1+0.05;
 				        
// 								segmentsLoopsRemoved.push_back(segments[i]);
// 					}

// 				}
// 			}
// 		}
	


// 		segments.clear();
// 		segments=segmentsLoopsRemoved;
// 		segmentsLoopsRemoved.clear();
// 		double sign;
		
// 		double Theta;
// 		int n_sprinklers=0; 
// 	   	double d=0;
					    
// 		for(size_t i = 0;i < segments.size()-1; i++)
// 			{

// 				auto  vertex_a=segments[i][1];
// 				auto  vertex_b = segments[i+1][0];
// 				auto tmp_vertex=vertex_a;
				
// 				dist = (vertex_a-vertex_b).norm();
// 				auto  vertex_a1=segments[i][0];
// 				auto  vertex_b1 = segments[i][1];
// 				dist1=(vertex_a1-vertex_b1).norm();
				
				


// 				if(dist>split1 || dist1>split1)  {

						
// 						if (dist1>split1) {
// 							tmp_vertex=vertex_a1;
// 							Theta=atan2((vertex_b1[1]-vertex_a1[1]),(vertex_b1[0]-vertex_a1[0]));
				
// 							n_sprinklers=static_cast<int>(dist1/split1);
// 							d=dist1/n_sprinklers;
// 						}
						
// 						if (dist>split1) {

// 							Theta=atan2((vertex_b[1]-vertex_a[1]),(vertex_b[0]-vertex_a[0]));
// 							if(Theta>=0) sign=-1.;
// 							tmp_vertex=vertex_a;
// 							n_sprinklers=static_cast<int>(dist/split1);
// 							d=dist/n_sprinklers;
// 						}



// 					        for (int i=0;i<n_sprinklers;i++) 
// 									{
//                             		std::cout<<"Atan,nsprinklers : " << Theta << "     " << n_sprinklers  << "\n";
//                             		Eigen::Vector2d a={tmp_vertex[0]+d*cos(Theta)*sign,tmp_vertex[1]+d*sin(Theta)*sign};
//                     			    segmentsLoopsRemoved.push_back({tmp_vertex,a});  
// 	                      			tmp_vertex=a;
//                         			}



// 						} else 
// 						{
// 							segmentsLoopsRemoved.push_back(segments[i]);
// 						}

				

// 			}



		
		
		
		
		

// 		segments.clear();	
// 		segments=segmentsLoopsRemoved;
// 		segmentsLoopsRemoved.clear();
// 		// ################################################## Triangles Addition - Start ##################################################3
		
// 		double dist2=0.;
// 		double dist3=0.;
// 		for(size_t i = 0;i < segments.size()-1; i++)
// 			{
// 				auto  vertex_a=segments[i][1];
// 				auto  vertex_b = segments[i+1][0];
// 				auto tmp_vertex=vertex_a;
				
// 				dist = (vertex_a-vertex_b).norm();
// 				auto  vertex_a1=segments[i][0];
// 				auto  vertex_b1 = segments[i][1];
// 				dist1=(vertex_a1-vertex_b1).norm();
// 				bool IsDist=(dist>=(split-1.5*delta)) && (dist<=(split+12.*delta));
// 				bool IsDist1=(dist1>=(split-1.5*delta)) && (dist1<=(split+12.*delta));
// 				IsDist=false;
// 				sign=1.0;
// 				printf("dist1: %f \n",dist1);
// 						if(IsDist1) 
// 							{	

// 									double x,y,x1,y1;
// 									double xUp,yUp;
									


// 									x=(vertex_a1[0]+vertex_b1[0])/2.-t*(vertex_b1[1]-vertex_a1[1]);
// 									y=(vertex_a1[1]+vertex_b1[1])/2.+t*(vertex_b1[0]-vertex_a1[0]);

// 									x1=(vertex_a1[0]+vertex_b1[0])/2.+t*(vertex_b1[1]-vertex_a1[1]);
// 									y1=(vertex_a1[1]+vertex_b1[1])/2.-t*(vertex_b1[0]-vertex_a1[0]);
									
									
									


// 									Eigen::Vector2d a={x,y};
// 									Eigen::Vector2d a1={x1,y1};
// 									dist2=(segments[i+1][1]-a).norm();
// 									dist3=(segments[i+1][1]-a1).norm();

// 									if(dist3>dist2) 
									
// 									{
// 										printf("dist3, dist2: %f,%f \n",dist3,dist2);
// 										x=x1;
// 										y=y1;

// 									}







// 									Eigen::Vector2d m={x,y};

// 									segmentsLoopsRemoved.push_back({vertex_a1,m});  
// 									segmentsLoopsRemoved.push_back({m,vertex_b1});  
							
// 							//sign=1.;




// 					} else {

// 							segmentsLoopsRemoved.push_back(segments[i]);

// 					}
				

// 			}

		


// 		segments.clear();
// 		segments=segmentsLoopsRemoved;

// 			// ################################################## Triangles Addition - End ##################################################3

	
// 		auto poses_proto = proto.initPoses(segments.size()*2);
// 		//std::vector<std::array<Eigen::Vector2d, 2>> segments = polygon_slice.Segments();;

// 		printf("\n\n\n");
// 		Pose2d waypoint;
// 		printf("Polygon Size : %i\n",segments.size());
		
// 		Eigen::Vector2d currV;

// 			double min_dist=10000.;
// 	int jj=0;
// 	for(size_t i = 0;i < segments.size(); i++){
	
// 			auto  v1=segments[i][0];
// 			auto  v2=segments[i][1];
// 			dist1=(v1-initialXY[0]).norm();

// 			if(dist1<min_dist)
// 			{
// 				printf("min_dist, %i, ,%i, %f \n",initialXY.size(),i,dist1);
// 				min_dist=dist1;
// 				jj=i;
				

// 			}



// 	}			
// 	//std::rotate(segments.begin(),segments.begin()+jj,segments.end());


		
// 		for(size_t i = 0;i < segments.size(); i++){
// 			waypoint.translation = segments[i][0];
	
// 			waypoint.rotation = waypoint.rotation.FromDirection(segments[i][1]-segments[i][0]);

// 			SO2d angle=waypoint.rotation;
// 			Vector2d t=segments[i][0];
// 			ToProto(waypoint,poses_proto[i*2]);
// 			waypoint.translation = segments[i][1];
// 			waypoint.rotation = waypoint.rotation.FromDirection(segments[i][1]-segments[i][0]);
// 			if( i< (segments.size()-1) ) 
// 			{
// 				//dist = (segments[i][0]-segments[i+1][0]).squaredNorm();
// 				dist = (segments[i][0]-segments[i+1][0]).norm();
// 				if (dist<eps) 
// 				{
// 					loop=1;

// 				} 
// 				else 
// 				{
// 					loop=0;
// 				}

// 			}

// 			SO2d angle1=waypoint.rotation;
// 			Vector2d t1=segments[i][1];
// 			printf("(x0,y0),(x1,y1),(angle0,angle1) - (%f,%f),  (%f,%f), (%f,%f),  (%f,%f),%i : \n",t[0],t[1],t1[0],t1[1],angle.cos(),angle.sin(),angle1.cos(),angle1.sin(), loop);

// 			ToProto(waypoint,poses_proto[(i*2)+1]);
			
// 			//if()
// 			auto  v1=segments[i][0];
// 			auto  v2=segments[i][1];
// 			dist1=(v1-initialXY[0]).norm();

// 			if(dist1<min_dist)
// 			{
// 				printf("min_dist, %i, ,%i, %f \n",initialXY.size(),i,dist1);
// 				min_dist=dist1;
// 				waypoint.translation = v1;
// 				currV=v1;
// 				f2=v2;
// 				f1=v1;
				
// 			//	v
// 			}



// /*
// 			if(i==segments.size()-1){
// //			if(i==0){
// 				auto goal_pose = goal_proto.initGoal();
// 				//waypoint.rotation = waypoint.rotation.FromDirection(segments[i][1]-segments[i][0]);
// 				//waypoint.translation=currV;
// 				//waypoint.translation=initialXY[0];
// 				waypoint.translation={0.,0.};
// 				printf("min_dist,  %f \n",min_dist);
// 				waypoint.rotation = waypoint.rotation.FromDirection(f2-f1);
// 				ToProto(waypoint,goal_pose);
// 				goal_proto.setTolerance(0.2);
// 				goal_proto.setGoalFrame("world");
// 				goal_proto.setStopRobot(true);
// 			}
// 			*/
// 		}
// 		proto.setPlanFrame("world");
// 		tx_plan().publish();
// //		tx_goal().publish();
// 		state=Navigating;
































    // printf("\n\nPATH");
    // for(int i = 0; i < path_polygon::m_vertices.size(); i++)
    // {
    //     printf("\n%i:\tx:%f\ty:%f", i, path_polygon.m_vertices.x(), path_polygon.m_vertices.y());
    // }

    // Mandoline::Graph polygon1 { Mandoline::Graph::Regular(20, 200.0) };
    // Mandoline::Graph polygon2 { Mandoline::Graph::Regular(20, 200.0) };
    // Mandoline::Graph polygon3 { Mandoline::Graph::Regular(20, 200.0) };

    // Eigen::Affine2d root = Eigen::Affine2d::Identity() * Eigen::Translation2d(720, 450);

    // Mandoline::Transform(polygon1, root * Eigen::Translation2d(100.0, 0.0)).Compute(polygon1);
    // Mandoline::Transform(polygon2, root * Eigen::Translation2d(-150.0, -150.0)).Compute(polygon2);
    // Mandoline::Transform(polygon3, root * Eigen::Translation2d(-100.0, 100.0)).Compute(polygon3);

    // Mandoline::Graph polygon_union;

    // Mandoline::Union(polygon1, polygon2).Compute(polygon_union);
    // Mandoline::Union(polygon_union, polygon3).Compute(polygon_union);

    // Mandoline::Graph polygon_slice;

    // Mandoline::Slice(polygon_union, 20.0).Compute(polygon_slice);
    
    // auto surface = Cairo::ImageSurface::create(Cairo::FORMAT_ARGB32, 1440, 900);
    // auto context = Cairo::Context::create(surface);
    // auto font = Cairo::ToyFontFace::create("Bitstream Charter", Cairo::FontSlant::FONT_SLANT_NORMAL, Cairo::FontWeight::FONT_WEIGHT_BOLD);

    // context->set_source_rgba(1.0, 1.0, 1.0, 1.0);
    // context->paint();

    // context->set_line_width(5.0);

    // int i = 0;

    // for (auto [vertex_a, vertex_b] : polygon_slice.Segments()) {
    //     context->set_source_rgba(1.0, 0.0, 0.0, 1.0);
    //     context->move_to(vertex_a.x(), vertex_a.y());
    //     context->line_to(vertex_b.x(), vertex_b.y());
    //     context->stroke();

    //     Eigen::Vector2d v = (vertex_a + vertex_b) * 0.5 + Eigen::Hyperplane<double, 2>::Through(vertex_a, vertex_b).normal() * 10.0;

    //     context->set_source_rgba(0.0, 0.0, 1.0, 1.0);
    //     context->move_to(v.x(), v.y());
    //     context->show_text(std::to_string(++i).c_str());
    // }

    // surface->write_to_png("slice.png");
    
    return 0;
}

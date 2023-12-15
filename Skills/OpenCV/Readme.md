# OpenCV
> 运作模式就是大量正负相关的样本训练精确度更好的分类器(xml文件 CascadeClassifier)，再以此编写逻辑

## 安装试运行 图片浏览器
> [arch安装opencv](https://my.oschina.net/u/4125051/blog/3071866)

1. sudo pacman -S  opencv vtk hdf5 cmake 
    - `CMakeLists.txt`
    ```c
    cmake_minimum_required(VERSION 2.10)
    project(test)
    find_package(OpenCV REQUIRED)
    add_executable(test main.cpp)
    target_link_libraries(test ${OpenCV_LIBS})
    ```
    ```cpp
    #include <iostream>
    #include <opencv4/opencv2/opencv.hpp>
    #include <opencv4/opencv2/highgui.hpp>
    #include <opencv4/opencv2/core.hpp>
    #include <opencv2/core.hpp>
    using namespace cv;
    using namespace std;
    int main()
    {
        string filename = "/path/to/pic.jpg";
        Mat img = imread(filename);
        auto size = img.size();
        int w = size.width;
        int h = size.height;
        Mat re_image;
        resize(img,re_image,Size(w*2, h*2));
        while(true)
        {
            imshow(filename,re_image);
            int k = waitKey(0);
            if(k == 27){
                break;
            }
        }
        destroyAllWindows();
    }
    ```
1. cmake . 
1. make 

************************

## gocv
> [gocv linux](https://gocv.io/getting-started/linux/) 

> [facedetect demo](https://github.com/hybridgroup/gocv/blob/master/cmd/facedetect/main.go)  

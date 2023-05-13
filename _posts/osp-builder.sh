# get Rocky 9 up and running, build OSPRay

# source this

sudo yum install vim
sudo yum install git
sudo yum install gcc
sudo yum install cmake.x86_64
sudo yum install tbb.x86_64 tbb-devel.x86_64
mkdir ~/src
cd ~/src
git clone https://github.com/ospray/ospray.git
cd ospray
mkdir build
cd build
cmake ${HOME}/src/ospray/scripts/superbuild
echo now "cmake --build -DOSPRAY_ENABLE_APPS=OFF ."

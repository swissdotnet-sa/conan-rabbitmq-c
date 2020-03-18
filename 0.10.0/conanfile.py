
from conans import ConanFile, CMake, tools
import os

class RabbitmqCConan(ConanFile):
    name = 'rabbitmq-c'
    version = '0.10.0'
    license = 'MIT'
    homepage = 'https://github.com/alanxz/rabbitmq-c'
    description = 'RabbitMQ C AMQP client library'
    author = 'Simon Lepasteur <simon.lepasteur@swissdotnet.ch>'
    url = 'https://github.com/swissdotnet-sa/conan-rabbitmq-c'
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    _archive_subfolder = homepage.rsplit('/', 1)[-1] + "-" + version
    _source_subfolder = "source_subfolder"
    
    
    def source(self):
        source_url = self.homepage
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="6455efbaebad8891c59f274a852b75b5cc51f4d669dfc78d2ae7e6cc97fcd8c0")
        os.rename(self._archive_subfolder, self._source_subfolder)
        
    
    # Library requirements.
    #def requirements(self):
    #    self.requires("boost/[>=1.69.0]")

        
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        #cmake.parallel = False
        #cmake.test()
        cmake.install()
        
    # You can choose to use package instead of the install step in build to have better control over what is included in the package.    
    #def package(self):
    #    self.copy("*.h", dst="include", src=os.path.join(self._source_subfolder, "include"))
    #    self.copy("*.lib", dst="lib", keep_path=False)
    #    self.copy("*.dll", dst="bin", keep_path=False)
    #    self.copy("*.so", dst="lib", keep_path=False)
    #    self.copy("*.dylib", dst="lib", keep_path=False)
    #    self.copy("*.a", dst="lib", keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

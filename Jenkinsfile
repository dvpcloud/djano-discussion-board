pipeline{
    agent {
       
        }           
    }
    stages {
            stage("Build docker image"){
                  when {
                      branch master
                  }                  
                  steps{
                    def  app_image = docker.build("django:${env.BUILD_ID}")  
                                     
                  }
            }
    }
}

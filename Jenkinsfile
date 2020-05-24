pipeline{
    agent {
        dockerfile{
            filename 'app_Dockerfile' 
        }           
    }
    stages {
            stage("Build docker image"){
                  when {
                      branch master
                  }                  
                  steps{
                      echo "completed"                     
                  }
            }
    }
}

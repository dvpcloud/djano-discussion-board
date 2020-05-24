pipeline{
    agent {
        dockerfile{
            filename 'app_Dockerfile'
            args '-t dvpcloud/dj-discuss'
        }
    }
    stages {
            stage("Build docker image"){
                  when {
                      branch master
                  }                  
                  steps{
                      sh 'python -V'                      
                  }
            }
    }
}

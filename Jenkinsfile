pipeline{   
    agent any
    stages {
            stage('Build docker image'){
                  when {
                      branch 'master'
                  }                  
                  steps{
                      script {

                            app_image = docker.build("dvpcloud/django:${env.BUILD_NUMBER}")
                            app_image.inside {
                                sh 'echo ${curl 127.0.0.1:8000)'
                            }  
                      }                
                  }
            }
            stage ('Push Docker Image') {
                when {
                    branch 'master'
                }
                steps{
                    script{
                        docker.withRegistry('https://registry.hub.docker.com','docker_hub') {
                            app_image.push("dvpcloud/django:${env.BUILD_ID}")
                        }
                    }
                }
            }

    }
}

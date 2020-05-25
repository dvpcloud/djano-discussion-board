pipeline{   
    agent any
    stages {
            stage('Build docker image'){                                  
                  steps{
                      script {

                            app_image = docker.build("dvpcloud/django:${env.BUILD_NUMBER}")                             
                        }                
                    }
               }
            stage ('Push Docker Image') {                
                steps {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com','docker_hub') {
                            app_image.push()
                        }
                    }
                }
            }
            stage('pull docker image') {
                agent {
                    docker { 
                        image "dvpcloud/django:${env.BUILD_NUMBER}"
                        
                        }
                }
                steps{
                    sh 'echo check '
                }
            }

    }
}

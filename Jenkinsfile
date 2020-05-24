pipeline{
    agent any
    stages {
            stage("Build docker image"){
                  when {
                      branch master
                  }
                  agent {
                      docker {
                          image 'python:3.8.2-alpine'
                      }           
                  }
                  steps{
                      sh 'echo python -V'
                      sh "echo $PATH"
                  }
            }
    }
}

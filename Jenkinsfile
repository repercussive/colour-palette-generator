pipeline {
  agent any
  stages {
    stage('Run unit tests') {
      steps {
        sh "bash scripts/run-unit-tests.sh"
      }
    }
    stage('Build and push Docker images') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DH_PASSWORD', usernameVariable: 'DH_USERNAME')]) {
          sh "bash scripts/build-docker-images.sh"
        }
      }
    }
    stage('Deploy app') {
      steps {
        sh "bash scripts/deploy.sh"
      }
    }
  }
}
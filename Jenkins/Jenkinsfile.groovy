pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                sh  'python3 -m pytest --junitxml build/report.xml tests/'
            }
        }

        stage('Integration') {
            junit 'build/report.xml'
        }
    }
}
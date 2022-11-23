pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                bat 'pytest --junitxml build\\report.xml tests\\'
                junit 'build\\report.xml'
            }
        }
    }
}
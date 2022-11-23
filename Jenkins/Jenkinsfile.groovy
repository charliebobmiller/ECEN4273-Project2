pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                bat 'python -m pytest --junitxml build\\report.xml tests\\'
                junit 'build\\report.xml'
            }
        }
    }
}
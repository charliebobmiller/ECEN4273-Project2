pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                pytest --junitxml build\\report.xml tests\\
                junit 'build\\report.xml'
            }
        }
    }
}
plugins {
    id("java")
    id("org.jetbrains.intellij") version "1.11.0"
}

group = "io.peerislands"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

java {
    sourceCompatibility = JavaVersion.VERSION_11
}

// Configure Gradle IntelliJ Plugin
// Read more: https://plugins.jetbrains.com/docs/intellij/tools-gradle-intellij-plugin.html
intellij {
    version.set("2022.1.4")
    type.set("IC") // Target IDE Platform

    plugins.set(listOf(/* Plugin Dependencies */))
}

tasks {
    buildSearchableOptions {
        enabled = false
    }
    // Set the JVM compatibility versions
    withType<JavaCompile> {
        sourceCompatibility = "11"
        targetCompatibility = "11"
    }

    patchPluginXml {
        version.set("${project.version}")
        sinceBuild.set("213")
        untilBuild.set("223.*")
    }

//    signPlugin {
//        certificateChain.set(System.getenv("CERTIFICATE_CHAIN"))
//        privateKey.set(System.getenv("PRIVATE_KEY"))
//        password.set(System.getenv("PRIVATE_KEY_PASSWORD"))
//    }

//    publishPlugin {
//        token.set(System.getenv("PUBLISH_TOKEN"))
//    }
}

dependencies {
    implementation("com.google.code.gson:gson:2.10")
    implementation("com.squareup.okhttp3:okhttp:4.10.0")

    //implementation("com.theokanning.openai-gpt3-java:api:0.8.1")
    implementation("com.theokanning.openai-gpt3-java:client:0.8.1")
}

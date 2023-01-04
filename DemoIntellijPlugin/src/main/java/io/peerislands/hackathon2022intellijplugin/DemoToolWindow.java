package io.peerislands.hackathon2022intellijplugin;

import java.io.File;
import java.io.IOException;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileSystemView;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.intellij.openapi.wm.ToolWindow;
import net.minidev.json.JSONObject;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class DemoToolWindow {

    private JPanel demoToolWindowContent;
    private JTabbedPane jTabbedPane;
    private JTabbedPane jTabbedPaneTabbedPane1;
    private JTabbedPane jTabbedPaneTabbedPane2;
    private JPanel jTabbedPane1JPanel1;
    private JPanel jPanel1JPanel1;
    private JLabel jPanel1LabelUrl;
    private JTextField jPanel1TextFieldUrl;
    private JScrollPane jPanel1JPanel1JScrollPane1;
    private JButton jPanel1Button1;
    private JTextArea jPanel1TextArea1;

    private JPanel jTabbedPane1JPanel2;
    private JPanel jPanel2JPanel1;
    private JLabel jPanel2LabelUrl;
    private JTextField jPanel2TextFieldUrl;
    private JButton jPanel2Button1;
    private JTextArea jPanel2TextArea1;

    private JPanel jTabbedPane1JPanel3;
    private JPanel jPanel3JPanel1;
    private JLabel jPanel3LabelUrl;
    private JLabel jPanel3Label2;
    private JLabel jPanel3Label3;
    private JTextField jPanel3TextFieldUrl;
    private JTextField jPanel3TextField2;
    private JTextField jPanel3TextField3;
    private JButton jPanel3Button1;
    private JTextArea jPanel3TextArea1;

    private JPanel jTabbedPane1JPanel4;
    private JPanel jPanel4JPanel1;
    private JLabel jPanel4LabelUrl;
    private JLabel jPanel4Label2;
    private JLabel jPanel4Label3;
    private JTextField jPanel4TextFieldUrl;
    private JTextField jPanel4TextField2;
    private JButton jPanel4BrowseButton;
    private JTextField jPanel4TextField3;
    private JTextArea jPanel4TextArea1;
    private JFileChooser jPanel4FileChooser;
    private JButton jPanel4Button1;

    private JPanel jTabbedPane1JPanel5;
    private JPanel jPanel5JPanel1;
    private JLabel jPanel5LabelUrl;
    private JLabel jPanel5Label2;
    private JLabel jPanel5Label3;
    private JTextField jPanel5TextFieldUrl;
    private JTextField jPanel5TextField2;
    private JButton jPanel5BrowseButton;
    private JTextField jPanel5TextField3;
    private JTextArea jPanel5TextArea1;
    private JFileChooser jPanel5FileChooser;
    private JButton jPanel5Button1;

    private JPanel jTabbedPane1JPanel6;
    private JPanel jPanel6JPanel1;
    private JLabel jPanel6LabelUrl;
    private JLabel jPanel6Label2;
    private JLabel jPanel6Label3;
    private JTextField jPanel6TextFieldUrl;
    private JTextField jPanel6TextField2;
    private JButton jPanel6BrowseButton;
    private JTextField jPanel6TextField3;
    private JTextArea jPanel6TextArea1;
    private JFileChooser jPanel6FileChooser;
    private JButton jPanel6Button1;

    private JPanel jTabbedPane2JPanel1;
    private JScrollPane openAIChatGptJScrollPane1;
    private JButton openAIChatGptSendButton1;
    private JTextArea openAIChatGptTextArea2;
    private JTextField openAIChatGptTextField1;


    Gson gson = new GsonBuilder().setPrettyPrinting().create();
    public DemoToolWindow(final ToolWindow toolWindow) {
        jPanel1Button1.addActionListener(e -> {
            try {
                sendGetAllTrainedModel();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });

        jPanel2Button1.addActionListener(e -> {
            try {
                sendGetTrainedModelById();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });

        jPanel3Button1.addActionListener(e -> {
            try {
                sendPostSentimentAnalysis();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });

        jPanel4BrowseButton.addActionListener(e -> {
            jPanel4JBrowseButtonActionPerformed();
        });

        jPanel4Button1.addActionListener(e -> {
            try {
                sendPostAudioTextAnalysis();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });

        jPanel5BrowseButton.addActionListener(e -> {
            jPanel5BrowseButtonActionPerformed();
        });

        jPanel5Button1.addActionListener(e -> {
            try {
                sendPostTrainModel();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });

        jPanel6BrowseButton.addActionListener(e -> {
            jPanel6BrowseButtonActionPerformed();
        });

        jPanel6Button1.addActionListener(e -> {
            try {
                sendPostReTrainModel();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });

        openAIChatGptSendButton1.addActionListener(e -> {
            try {
                openAIChatGPT();
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        });
    }

    private void jPanel4JBrowseButtonActionPerformed() {
        jPanel4FileChooser = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());
        jPanel4FileChooser.setDialogTitle("Select an audio file to analyse:");
        jPanel4FileChooser.setMultiSelectionEnabled(false);
        jPanel4FileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        jPanel4FileChooser.setAcceptAllFileFilterUsed(false);
        FileNameExtensionFilter filter = new FileNameExtensionFilter("WAV", "wav");
        jPanel4FileChooser.addChoosableFileFilter(filter);
        if (jPanel4FileChooser.showDialog(null, "Upload File") == JFileChooser.APPROVE_OPTION) {
            jPanel4TextField2.setText(jPanel4FileChooser.getSelectedFile().getAbsolutePath());
        }
    }

    private void jPanel5BrowseButtonActionPerformed() {
        jPanel5FileChooser = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());
        jPanel5FileChooser.setDialogTitle("Select a file to train model:");
        jPanel5FileChooser.setMultiSelectionEnabled(false);
        jPanel5FileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        jPanel5FileChooser.setAcceptAllFileFilterUsed(false);
        FileNameExtensionFilter filter = new FileNameExtensionFilter("CSV", "csv");
        jPanel5FileChooser.addChoosableFileFilter(filter);
        if (jPanel5FileChooser.showDialog(null, "Upload File") == JFileChooser.APPROVE_OPTION) {
            jPanel5TextField2.setText(jPanel5FileChooser.getSelectedFile().getAbsolutePath());
        }
    }

    private void jPanel6BrowseButtonActionPerformed() {
        jPanel6FileChooser = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());
        jPanel6FileChooser.setDialogTitle("Select a file to retrain model:");
        jPanel6FileChooser.setMultiSelectionEnabled(false);
        jPanel6FileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        jPanel6FileChooser.setAcceptAllFileFilterUsed(false);
        FileNameExtensionFilter filter = new FileNameExtensionFilter("CSV", "csv");
        jPanel6FileChooser.addChoosableFileFilter(filter);
        if (jPanel6FileChooser.showDialog(null, "Upload File") == JFileChooser.APPROVE_OPTION) {
            jPanel6TextField2.setText(jPanel6FileChooser.getSelectedFile().getAbsolutePath());
        }
    }

    private void sendGetAllTrainedModel() throws IOException, InterruptedException {
        String url = jPanel1TextFieldUrl.getText();

        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("text/plain");
        MediaType JSON = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(JSON, "{}");
        Request request = new Request.Builder()
                .url(url)
                .method("GET", null)
                .build();
        Response response = client.newCall(request).execute();

        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        String prettyJsonString = gson.toJson(jsonElement);
//        System.out.println(prettyJsonString);
        jPanel1TextArea1.setText(prettyJsonString);
    }

    private void sendGetTrainedModelById() throws IOException, InterruptedException {
        String url = jPanel2TextFieldUrl.getText();

        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("text/plain");
        MediaType JSON = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(JSON, "{}");
        Request request = new Request.Builder()
                .url(url)
                .method("GET", null)
                .build();
        Response response = client.newCall(request).execute();

        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        String prettyJsonString = gson.toJson(jsonElement);
//        System.out.println(prettyJsonString);
        jPanel2TextArea1.setText(prettyJsonString);
    }

    private void sendPostSentimentAnalysis() throws IOException, InterruptedException {
        String url = jPanel3TextFieldUrl.getText();
        String modelToUse = jPanel3TextField2.getText();
        String textToAnalyse = jPanel3TextField3.getText();

        JSONObject jsonObject = new JSONObject();
        jsonObject.put("model_to_use", modelToUse);
        jsonObject.put("text", textToAnalyse);

        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("application/json");
        RequestBody body = RequestBody.create(mediaType, jsonObject.toJSONString());
        Request request = new Request.Builder()
                .url(url)
                .method("POST", body)
                .addHeader("Content-Type", "application/json")
                .build();
        Response response = client.newCall(request).execute();


        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        String prettyJsonString = gson.toJson(jsonElement);
//        System.out.println(prettyJsonString);
        jPanel3TextArea1.setText(prettyJsonString);
    }

    private void sendPostAudioTextAnalysis() throws IOException, InterruptedException {
        String url = jPanel4TextFieldUrl.getText();
        String filePath = jPanel4TextField2.getText();
        String data = jPanel4TextField3.getText();

        String[] filePathSpliArray = filePath.split("/");
        String fileName = filePathSpliArray[filePathSpliArray.length - 1];

        OkHttpClient client = new OkHttpClient().newBuilder().build();
        MediaType mediaType = MediaType.parse("text/plain");
        RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM).addFormDataPart("file",fileName,
                        RequestBody.create(new File(filePath), MediaType.parse("application/octet-stream")))
                .addFormDataPart("data",data)
                .build();
        Request request = new Request.Builder().url(url).method("POST", body).build();
        Response response = client.newCall(request).execute();

        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        String prettyJsonString = gson.toJson(jsonElement);
//        System.out.println(prettyJsonString);
        jPanel4TextArea1.setText(prettyJsonString);
    }

    private void sendPostTrainModel() throws IOException, InterruptedException {
        String url = jPanel5TextFieldUrl.getText();
        String filePath = jPanel5TextField2.getText();
        String data = jPanel5TextField3.getText();

        String[] filePathSpliArray = filePath.split("/");
        String fileName = filePathSpliArray[filePathSpliArray.length - 1];

        OkHttpClient client = new OkHttpClient().newBuilder().build();
        MediaType mediaType = MediaType.parse("text/plain");
        RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM).addFormDataPart("file",fileName,
                        RequestBody.create(new File(filePath), MediaType.parse("application/octet-stream")))
                .addFormDataPart("data",data)
                .build();
        Request request = new Request.Builder().url(url).method("POST", body).build();
        Response response = client.newCall(request).execute();

        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        String prettyJsonString = gson.toJson(jsonElement);
//        System.out.println(prettyJsonString);
        jPanel5TextArea1.setText(prettyJsonString);
    }

    private void sendPostReTrainModel() throws IOException, InterruptedException {
        String url = jPanel6TextFieldUrl.getText();
        String filePath = jPanel6TextField2.getText();
        String data = jPanel6TextField3.getText();

        String[] filePathSpliArray = filePath.split("/");
        String fileName = filePathSpliArray[filePathSpliArray.length - 1];

        OkHttpClient client = new OkHttpClient().newBuilder().build();
        MediaType mediaType = MediaType.parse("text/plain");
        RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM).addFormDataPart("file",fileName,
                        RequestBody.create(new File(filePath), MediaType.parse("application/octet-stream")))
                .addFormDataPart("data",data)
                .build();
        Request request = new Request.Builder().url(url).method("POST", body).build();
        Response response = client.newCall(request).execute();

        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        String prettyJsonString = gson.toJson(jsonElement);
//        System.out.println(prettyJsonString);
        jPanel6TextArea1.setText(prettyJsonString);
    }

    private void openAIChatGPT() throws IOException, InterruptedException {
        String textToSearch = openAIChatGptTextField1.getText();

        String openAIUrl = "https://api.openai.com/v1/completions";
        JSONObject bodyJsonObject = new JSONObject();
        bodyJsonObject.put("model", "text-davinci-003");
        bodyJsonObject.put("prompt", textToSearch);
        bodyJsonObject.put("temperature", 0);
        bodyJsonObject.put("max_tokens", 500);

        OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("application/json");
        RequestBody body = RequestBody.create(mediaType, bodyJsonObject.toJSONString());
        Request request = new Request.Builder()
                .url(openAIUrl)
                .method("POST", body)
                .addHeader("Authorization", "Bearer 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")
                .addHeader("Content-Type", "application/json")
                .build();
        Response response = client.newCall(request).execute();
        JsonElement jsonElement = JsonParser.parseString(response.body().string());
        JsonObject responseJsonObject = jsonElement.getAsJsonObject();
        JsonObject choicesJsonObject = responseJsonObject.getAsJsonArray("choices").get(0).getAsJsonObject();
        String responseText = choicesJsonObject.get("text").getAsString();
        openAIChatGptTextArea2.setText(responseText);
//        String[] responseTextLineArray = responseText.split("\n");
//        StringBuffer responseSb = new StringBuffer();
//        for(String line: responseTextLineArray) {
//            String[] lineWordArray = line.split(" ");
//            for(String word: lineWordArray) {
//                responseSb.append(word);
//                jPanel2TextArea1.setText(responseSb.toString());
//                Thread.sleep(100);
//            }
//            responseSb.append("\n");
//            Thread.sleep(100);
//        }
    }

    public JPanel getContent() {
        return demoToolWindowContent;
    }

}


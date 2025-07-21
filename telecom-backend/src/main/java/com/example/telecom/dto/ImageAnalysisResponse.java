package com.example.telecom.dto;

public class ImageAnalysisResponse {
    private String problemDetected;

    public ImageAnalysisResponse() {
    }

    public ImageAnalysisResponse(String problemDetected) {
        this.problemDetected = problemDetected;
    }

    public String getProblemDetected() {
        return problemDetected;
    }

    public void setProblemDetected(String problemDetected) {
        this.problemDetected = problemDetected;
    }
}

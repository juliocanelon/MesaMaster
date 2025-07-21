package com.example.telecom.service;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
public class ImageAnalysisService {
    public String analyzeImage(MultipartFile file) {
        // TODO: Integrate real image analysis logic here.
        return "Detected broken antenna";
    }
}

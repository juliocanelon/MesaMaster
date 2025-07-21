package com.example.telecom.controller;

import com.example.telecom.dto.ImageAnalysisResponse;
import com.example.telecom.service.ImageAnalysisService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/")
public class ImageAnalysisController {

    private final ImageAnalysisService imageAnalysisService;

    public ImageAnalysisController(ImageAnalysisService imageAnalysisService) {
        this.imageAnalysisService = imageAnalysisService;
    }

    @PostMapping(path = "/analyze-image", consumes = "multipart/form-data")
    public ResponseEntity<ImageAnalysisResponse> analyzeImage(@RequestParam("image") MultipartFile imageFile) {
        if (imageFile.isEmpty()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Image file is required");
        }

        String result = imageAnalysisService.analyzeImage(imageFile);
        return ResponseEntity.ok(new ImageAnalysisResponse(result));
    }
}

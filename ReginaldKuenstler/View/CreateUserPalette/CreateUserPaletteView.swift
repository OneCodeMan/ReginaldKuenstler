import SwiftUI
import Vision
import PhotosUI
import Foundation

struct CreatePaletteWithPhotosView: View {
    @State private var recognizedText: String = ""
    @State private var showImagePicker = false
    @State private var showCamera = false
    @State private var selectedImage: UIImage?
    
    var body: some View {
        VStack {
            if let image = selectedImage {
                Image(uiImage: image)
                    .resizable()
                    .scaledToFit()
                    .frame(height: 300)
            } else {
                Text("Tap to select or capture an image")
                    .padding()
                    .foregroundColor(.gray)
                    .frame(height: 300)
                    .background(Color.secondary.opacity(0.1))
                    .cornerRadius(8)
                    .onTapGesture {
                        showImagePicker = true
                    }
            }
            
            Text("Recognized Colours:")
                .font(.headline)
                .padding(.top)
            
            ScrollView {
                Text(recognizedText.isEmpty ? "No text recognized" : recognizedText)
                    .padding()
                    .background(Color.secondary.opacity(0.1))
                    .cornerRadius(8)
            }
            .frame(height: 200)
            
            HStack {
                Button("Select from Library") {
                    showImagePicker = true
                }
                .padding()
                
                Button("Capture Photo") {
                    showCamera = true
                }
                .padding()
            }
        }
        .padding()
        .sheet(isPresented: $showImagePicker) {
            CreatePaletteImagePicker(selectedImage: $selectedImage, onImagePicked: recognizeText)
        }
        .fullScreenCover(isPresented: $showCamera) {
            CameraCaptureView(selectedImage: $selectedImage, onImageCaptured: recognizeText)
        }
    }
    
    // Text recognition function
    private func recognizeText(from image: UIImage) {
        guard let cgImage = image.cgImage else { return }
        
        let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
        let request = VNRecognizeTextRequest { request, error in
            guard error == nil else {
                recognizedText = "Text recognition failed: \(error!.localizedDescription)"
                return
            }
            
            if let results = request.results as? [VNRecognizedTextObservation] {
                let colourMap = ColourMapper.shared.colourMap
                recognizedText = results.compactMap { observation in
                    observation.topCandidates(1).first?.string
                }.joined(separator: "\n")
                
                // RAW TEXT
                // print(recognizedText)
                
                // Try to extract text
                
                // separate recognizedText at newLine
                let recognizedTextSplit = recognizedText.split(whereSeparator: \.isNewline)
                
                var arrayOfDetectedColourStrings: [String] = []
                
                for line in recognizedTextSplit {
                    let sanitizedLine = line.lowercased().trimmingCharacters(in: .whitespaces)
                    
                    // if we found a colour name that our colourMap recognizes.
                    if colourMap.contains(where: { $0.name.lowercased().trimmingCharacters(in: .whitespaces) == sanitizedLine }) {
                        print("HIP HIP HURRAY!!!: \(sanitizedLine)")
                        arrayOfDetectedColourStrings.append(sanitizedLine)
                    } else {
                        print("NOOOOO: \(sanitizedLine)")
                    }
                }
                
                arrayOfDetectedColourStrings = arrayOfDetectedColourStrings.uniqued()
                
                print("Number of hip-hip-hurrays: \(arrayOfDetectedColourStrings.count)\n")
                print("Hip-hip-hurrays:\n \(arrayOfDetectedColourStrings)")
                
                var detectedPaletteColours: [PaletteColour] = []
                // then make VColours out of `arrayOfDetectedColourStrings`
                for detectedColourString in arrayOfDetectedColourStrings {
                    if let vColourIndex = colourMap.firstIndex(where: { $0.name.lowercased() == detectedColourString }) {
                        let targetVColour: VColour = colourMap[vColourIndex]
                        let generatedPaletteColour: PaletteColour = PaletteColour(fromVColour: targetVColour)
                        detectedPaletteColours.append(generatedPaletteColour)
                    } else {
                        print("VColour Index not found .errorrrrrr")
                    }
                    
                }
                
                print("Detected palette colours:\n\n")
                for pc in detectedPaletteColours {
                    print(pc.colourName, pc.hexCode)
                }
                print("\n\n")
                
                
            } else {
                recognizedText = "No text found"
            }
        }
        
        request.recognitionLevel = .accurate
        request.usesLanguageCorrection = true
        
        DispatchQueue.global(qos: .userInitiated).async {
            do {
                try requestHandler.perform([request])
            } catch {
                DispatchQueue.main.async {
                    recognizedText = "Failed to perform request: \(error.localizedDescription)"
                }
            }
        }
    }
}

// Image picker helper for SwiftUI
struct CreatePaletteImagePicker: UIViewControllerRepresentable {
    @Binding var selectedImage: UIImage?
    var onImagePicked: (UIImage) -> Void

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    func makeUIViewController(context: Context) -> PHPickerViewController {
        var config = PHPickerConfiguration(photoLibrary: .shared())
        config.filter = .images
        config.selectionLimit = 1
        
        let picker = PHPickerViewController(configuration: config)
        picker.delegate = context.coordinator
        return picker
    }

    func updateUIViewController(_ uiViewController: PHPickerViewController, context: Context) {}

    class Coordinator: NSObject, PHPickerViewControllerDelegate {
        let parent: CreatePaletteImagePicker

        init(_ parent: CreatePaletteImagePicker) {
            self.parent = parent
        }

        func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
            picker.dismiss(animated: true)
            
            guard let result = results.first else { return }
            
            if result.itemProvider.canLoadObject(ofClass: UIImage.self) {
                result.itemProvider.loadObject(ofClass: UIImage.self) { (image, error) in
                    if let uiImage = image as? UIImage {
                        DispatchQueue.main.async {
                            self.parent.selectedImage = uiImage
                            self.parent.onImagePicked(uiImage)
                        }
                    }
                }
            }
        }
    }
}

// Camera capture helper for SwiftUI
struct CameraCaptureView: UIViewControllerRepresentable {
    @Binding var selectedImage: UIImage?
    var onImageCaptured: (UIImage) -> Void
    
    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    func makeUIViewController(context: Context) -> UIImagePickerController {
        let picker = UIImagePickerController()
        picker.sourceType = .camera
        picker.delegate = context.coordinator
        return picker
    }
    
    func updateUIViewController(_ uiViewController: UIImagePickerController, context: Context) {}

    class Coordinator: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
        let parent: CameraCaptureView

        init(_ parent: CameraCaptureView) {
            self.parent = parent
        }

        func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            picker.dismiss(animated: true)
            
            if let image = info[.originalImage] as? UIImage {
                DispatchQueue.main.async {
                    self.parent.selectedImage = image
                    self.parent.onImageCaptured(image)
                }
            }
        }

        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
            picker.dismiss(animated: true)
        }
    }
}

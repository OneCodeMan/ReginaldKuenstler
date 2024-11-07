import SwiftUI
import Vision
import PhotosUI
import Foundation

/**
 MARK: V0.2
 */
struct CreatePaletteWithPhotosView: View {
    @EnvironmentObject var userPaletteViewModel: UserPaletteViewModel

    @State private var recognizedText: String = ""
    @State private var showImagePicker = false
    @State private var showCamera = false
    @State private var selectedImage: UIImage?
    
    // MARK: State to track user input converted to palette colours
    @State var detectedPaletteColours: [PaletteColour] = []
    
    // MARK: Alert states
    @State var displayPaletteCreationConfirmation: Bool = false
    
    var body: some View {
        VStack {
            if let image = selectedImage {
                Image(uiImage: image)
                    .resizable()
                    .scaledToFit()
                    .frame(height: 300)
                
            } else {
                VStack {
                    Text("Tap to select or capture an image")
                        .padding()
                        .foregroundColor(.gray)
                        .frame(height: 300)
                        .background(Color.secondary.opacity(0.1))
                        .cornerRadius(8)
                        .onTapGesture {
                            showImagePicker = true
                        }
                        .overlay(
                            RoundedRectangle(cornerRadius: 16)
                                .strokeBorder(style: StrokeStyle(lineWidth: 4, dash: [10], dashPhase: 0.0))
                        )
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
            
            VStack {
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
        .sheet(isPresented: $displayPaletteCreationConfirmation) {
            PaletteCreationConfirmationView(paletteColours: $detectedPaletteColours) {

                // remove duplicates between userpalette and newcolours before adding colours to userpalette
                let coloursToSave = detectedPaletteColours.reduce(into: [String: String]()) { result, item in
                    // if userPalette already has current detected colour, do not add it to user palette again.
                    if userPaletteViewModel.userPaletteColours.contains(where: { $0.colourName.lowercased() == item.colourName.lowercased() }) {
                        print("NOT ADDING \(item.colourName) because userPalette already has it.")
                    } else {
                        result[item.colourName] = item.hexCode
                    }
                    
                }
                
                userPaletteViewModel.saveUserPaletteColours(coloursToSave)
            }
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
                // TODO: replace with v0.2 map
                let colourMap = ColourCatalog.shared.colourMap
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
                    if let catalogColourIndex = colourMap.firstIndex(where: { $0.name.lowercased() == detectedColourString }) {
                        let targetCatalogColour: CatalogColour = colourMap[catalogColourIndex]
                        let generatedPaletteColour: PaletteColour = PaletteColour(fromCatalogColour: targetCatalogColour)
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

                self.detectedPaletteColours = detectedPaletteColours
                displayPaletteCreationConfirmation = true
                
                // Saving palette to userdefaults handled by modal logic.
                
                
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

// MARK: Palette Creation Confirmation View
struct PaletteCreationConfirmationView: View {
    
    // MARK: State variables
    @Binding var paletteColours: [PaletteColour]
    var saveColoursToUserPalette: () -> ()
    
    // MARK: VGrid logic
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    // MARK: Booleans for dismissing/presenting alerts
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationStack {
            VStack {
                if !paletteColours.isEmpty {
                    List {
                        LazyVGrid(columns: columns) {
                            ForEach(paletteColours, id: \.self) { pc in
                                SingularPaletteItemView(paletteColour: pc)
                            }
                        }
                    }
                    
                } else {
                    Text("NO PALETTE COLOURS DETECTED")
                }
                
                VStack {
                    Button("Save to user defaults") {
                        self.saveColoursToUserPalette()
                        self.dismiss()
                    }
                    .padding()
                    Button("Try Again") {
                        self.dismiss()
                    }
                    .padding()
                }
            }
            .navigationTitle(Text(String(localized: "Add Colours to Palette")))
        }
        
    }
}

// MARK: Image picker helper for SwiftUI
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

// MARK: Camera capture helper
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

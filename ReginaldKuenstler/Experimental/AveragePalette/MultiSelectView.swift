import SwiftUI
import PhotosUI

struct MultiSelectView: View {
    @ObservedObject var viewModel = AveragePaletteViewModel()
    @State private var images: [UIImage] = [] // Array to hold selected images
    @State private var isPickerPresented: Bool = false
    
    @State private var displayMinimumPalette: Bool = false

    var rows = [
        GridItem(.flexible()) // Adjust the size as needed
    ]

    var body: some View {
        ScrollView {
            VStack {
                
                // images
                VStack {
                    
                    ScrollView(.horizontal) {
                        LazyHGrid(rows: rows, spacing: 10) {
                            ForEach(images, id: \.self) { image in
                                Image(uiImage: image)
                                    .resizable()
                                    .scaledToFit()
                                    .frame(minHeight: 200)
                                    .cornerRadius(8)
                                    .unredacted()
                            }
                        }
                        .padding()
                    } // end of scrollview
                    .frame(minHeight: 400, maxHeight: 450)
                    .redacted(reason: .placeholder)
                }
                
                // anal
                
                Divider()
                
                if viewModel.isLoading {
                    ProgressView("Analyzing images...")
                } else {
                    ScrollView(.horizontal) {
                        LazyHGrid(rows: rows, spacing: 10) {
                            ForEach(viewModel.paletteResults.indices, id: \.self) { index in
                                VStack {
                                    Image(uiImage: images[index])
                                        .resizable()
                                        .frame(width: 90, height: 60)
                                        .scaledToFill()
                                        .padding()
                                    Section {
                                        ForEach(viewModel.paletteResults[index]) { colour in
                                            HStack {
                                                Text(colour.colourName)
                                                    .frame(width: 100, alignment: .leading)
                                                
                                                Rectangle()
                                                    .fill(Color(colour.uiColour))
                                                    .frame(width: 30, height: 30)
                                                    .cornerRadius(5)
                                            }
                                        }
                                    } // end of Section
                                } // end of VStack
                                .unredacted()
                                .padding()
                                Divider().frame(width: 2)
                            } // end of ForEach
                        }
                        .padding(8)
                        
                    }
                    .redacted(reason: .placeholder)
                    
                    if displayMinimumPalette {
                        // Minimum Palette view
                        VStack {
                            Text("Minimum Palette")
                                .font(.defaultFontLargeTitle)
                            HStack {
                                let paletteToDisplay = viewModel.minimumPalette.colours.isEmpty ? Palette() : viewModel.minimumPalette
                                MinimumPaletteView(minimumPalette: paletteToDisplay, shouldOmitTitle: true)
                            }
                        }
                        .padding()
                        .unredacted()
                    }
                    
                    
                } // end oof if statement

                Button("Select Images") {
                    isPickerPresented.toggle()
                }
                .padding()
                .sheet(isPresented: $isPickerPresented) {
                    PHPickerViewControllerWrapper(images: $images)
                }

                Button("Analyze") {
                    self.displayMinimumPalette = true
                    Task {
                        await viewModel.analyzeImages(images: images)
                    }
                }
                .padding()

            }
        }
        
    }
}


struct PHPickerViewControllerWrapper: UIViewControllerRepresentable {
    @Binding var images: [UIImage]
    
    func makeUIViewController(context: Context) -> PHPickerViewController {
        var config = PHPickerConfiguration()
        config.selectionLimit = 0 // 0 means no limit
        config.filter = .images
        
        let picker = PHPickerViewController(configuration: config)
        picker.delegate = context.coordinator
        return picker
    }
    
    func updateUIViewController(_ uiViewController: PHPickerViewController, context: Context) {}

    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }

    class Coordinator: NSObject, PHPickerViewControllerDelegate {
        let parent: PHPickerViewControllerWrapper
        
        init(_ parent: PHPickerViewControllerWrapper) {
            self.parent = parent
        }
        
        func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
            picker.dismiss(animated: true)
            
            for result in results {
                if result.itemProvider.canLoadObject(ofClass: UIImage.self) {
                    result.itemProvider.loadObject(ofClass: UIImage.self) { object, error in
                        if let image = object as? UIImage {
                            DispatchQueue.main.async {
                                self.parent.images.append(image)
                            }
                        }
                    }
                }
            }
        }
    }
}

struct MinimumPaletteView: View {
    var minimumPalette: Palette
    @State var artistName: String = "Placeholder"
    @State var isFullScreen: Bool = false
    
    var shouldOmitTitle: Bool = false
    @Environment(\.colorScheme) var colorScheme
    
    // MARK: Fullscreen states for view
    private let columns = Array(repeating: GridItem(.flexible()), count: 3)

    var body: some View {
        VStack(alignment: .center) {
            if self.isFullScreen {
                ScrollView {
                    VStack {
                        Spacer()
                        if !shouldOmitTitle {
                            Text("The \(artistName) Palette")
                                .font(.defaultFontLargeTitle)
                                .padding(.bottom, 8)
                                .foregroundStyle(colorScheme == .dark ? .white : .black)
                        }
                        
                        LazyVGrid(columns: self.columns) {
                            ForEach(minimumPalette.colours, id: \.self) { pc in
                                SingularPaletteItemView(paletteColour: pc)
                            }
                        }
                        
                    }// .frame(minWidth: UIScreen.main.bounds.width)
                    
                }.frame(minWidth: UIScreen.main.bounds.width)
                
               
            } else {
                // NOT fullscreen
                
                // Bottom HStack
                HStack(alignment: .bottom) {
                    ForEach(Array(minimumPalette.colours.prefix(upTo: 6)), id: \.self) { pc in
                        SingularPaletteItemView(paletteColour: pc)
                            .opacity(0.2)
                    }
                    
                } // HStack
                .frame(maxWidth: .infinity)
                .frame(height: 50)
                .padding()
                
            }
             // end of else
            
        }
        .background(!shouldOmitTitle ? (isFullScreen ? Color.white.opacity(0.9) : Color.white.opacity(0.4)) : Color.black)
        .onTapGesture {
            withAnimation {
                self.isFullScreen.toggle()
            }
        }
        // VSTACK
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        MultiSelectView()
    }
}

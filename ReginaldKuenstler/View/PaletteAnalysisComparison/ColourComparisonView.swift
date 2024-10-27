//
//  ColourComparisonView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import SwiftUI
import SwiftVibrantium

// https://medium.com/@sharma17krups/onboarding-view-with-swiftui-b26096049be3
struct ColourComparisonView: View {
    @ObservedObject var viewModel = KuenstlerViewModel()
    @State var imgTitle = "Calum from Aftersun"
    @State var imgName = "starz"
    @State var infoString = "Title of Image"
    @State var paletteString = ""
    @State var personalPaletteString = ""
    
    @State var realColours: [UIColor] = Array(repeating: .clear, count: 6)
    @State var estimatedColours: [UIColor] = Array(repeating: .clear, count: 6)
    @State var coloursFromUserPalette: [UIColor] = Array(repeating: .clear, count: 6)
    
    // MARK: Image states
    @State private var image = UIImage(named: "beauty") ?? UIImage()
    @State private var showSheet = false
    @State private var showImagePicker = false
    @State private var sourceType: UIImagePickerController.SourceType = .photoLibrary
    
    @State var views: [CarouselPage] = []
    
    // MARK: Boolean view states
    @State private var disableScrollNoImageInput: Bool = true
    
    // Control current page index
    @State private var currentIndex = 0
    
    var body: some View {
        VStack {
            // TabView with Carousel Pages
            TabView(selection: $currentIndex) {
                CarouselPage(id: 0, content: {
                    ImageAnalysisInputView(image: $image, showSheet: $showSheet, showImagePicker: $showImagePicker, sourceType: $sourceType, handleAnalyzePhoto: {
                        self.performColourAnalysis(onImage: self.image)
                        withAnimation {
                            if currentIndex == 0 {
                                self.currentIndex = 1
                            }
                        }
                    })
                })
                .padding(.bottom, 20)
                .tag(0)
                
                CarouselPage(id: 1, content: {
                    PaletteResults(realColours: $realColours, paletteString: $paletteString, coloursFromUserPalette: $coloursFromUserPalette, personalPaletteString: $personalPaletteString, isLoading: $viewModel.isLoading, disableScrollNoImageInput: $disableScrollNoImageInput)
                })
                .tag(1)
            }
            .tabViewStyle(PageTabViewStyle())
            .padding(.vertical, 20)
        }
        .onAppear {
            self.views = [
                CarouselPage(id: 0, content: {
                    ImageAnalysisInputView(image: $image, showSheet: $showSheet, showImagePicker: $showImagePicker, sourceType: $sourceType, handleAnalyzePhoto: {
                        self.performColourAnalysis(onImage: self.image)
                    })
                }),
                CarouselPage(id: 1, content: {
                    PaletteResults(realColours: $realColours, paletteString: $paletteString, coloursFromUserPalette: $coloursFromUserPalette, personalPaletteString: $personalPaletteString, isLoading: $viewModel.isLoading, disableScrollNoImageInput: $disableScrollNoImageInput)
                })
            ]
        }
    }
    
    func performColourAnalysis(onImage img: UIImage) {
        // Reset palette strings
        paletteString = ""
        personalPaletteString = ""
        let artwork = Artwork(image: img, title: imgTitle)
        
        viewModel.performAnalOnImage(artwork: artwork) { colourPairs, relevantColoursFromUserPalette in
            DispatchQueue.main.async {
                // Update real and estimated colours
                for i in 0..<min(colourPairs.count, realColours.count) {
                    realColours[i] = colourPairs[i].actualColourInfo.uiColour
                    estimatedColours[i] = colourPairs[i].estimatedColourInfo.uiColour
                    paletteString += "\(colourPairs[i].name), "
                }
                
                // Update user palette
                if !relevantColoursFromUserPalette.isEmpty {
                    for j in 0..<min(relevantColoursFromUserPalette.count, coloursFromUserPalette.count) {
                        coloursFromUserPalette[j] = relevantColoursFromUserPalette[j].uiColour
                        personalPaletteString += "\(relevantColoursFromUserPalette[j].name), "
                    }
                } else {
                    coloursFromUserPalette = []
                    personalPaletteString = "No relevant colours found."
                }
            }
        }
    }
}

// first page in carousel
struct ImageAnalysisInputView: View {
    @Binding var image: UIImage
    @Binding var showSheet: Bool
    @Binding var showImagePicker: Bool
    @Binding var sourceType: UIImagePickerController.SourceType
    var handleAnalyzePhoto: () -> ()
    
    var body: some View {
        ZStack(alignment: .top) {
            VStack {
                Spacer()
                    .frame(height: 50)
                
                // TODO: if no image input, add a placeholder image.
                Image(uiImage: self.image)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .clipShape(RoundedRectangle(cornerRadius: 10))
                    .overlay(
                        Rectangle()
                            .stroke(Color.brownOuterFrameImage, lineWidth: 12)
                            .border(Color.goldInnerFrameImage, width: 14)
                    )
                    .edgesIgnoringSafeArea(.all)
                    .statusBar(hidden: true)
                    .padding()
            }
            
            VStack {
                Text("Change photo")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1)))
                    .cornerRadius(3)
                    .foregroundColor(.white)
                    .padding(.horizontal, 10)
                    .onTapGesture {
                        showSheet = true
                    }
                
                Text("Analyze")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1)))
                    .cornerRadius(3)
                    .foregroundColor(.white)
                    .padding(.horizontal, 10)
                    .onTapGesture {
                        print("Analyze button tapped, performing analysis on \(self.image)")
                        handleAnalyzePhoto()
                    }
            }
            .padding()
            .frame(maxHeight: .infinity, alignment: .bottom)
        }
        .actionSheet(isPresented: $showSheet) {
            ActionSheet(title: Text("Select Photo"), message: Text("Choose an option"), buttons: [
                .default(Text("Take Photo")) {
                    self.sourceType = .camera
                    self.showImagePicker = true
                },
                .default(Text("Select from Library")) {
                    self.sourceType = .photoLibrary
                    self.showImagePicker = true
                },
                .cancel()
            ])
        }
        .sheet(isPresented: $showImagePicker) {
            ImagePicker(sourceType: self.sourceType, selectedImage: self.$image)
        }
    }
}

// second page in carousel
struct PaletteResults: View {
    @Binding var realColours: [UIColor]
    @Binding var paletteString: String
    @Binding var coloursFromUserPalette: [UIColor]
    @Binding var personalPaletteString: String
    @Binding var isLoading: Bool
    @Binding var disableScrollNoImageInput: Bool
    var body: some View {
            if isLoading {
                VStack {
                    Spacer()
                    ProgressView() {
                        Text("Loading")
                            .font(.title)
                    }
                    .progressViewStyle(.circular)
                    Spacer()
                }
            } else {
            ScrollView {
                VStack(alignment: .center) {
                    Text("Detected Colours")
                        .font(.title2)
                        .bold()
                    
                    HStack(spacing: 0) {
                        ForEach(0..<realColours.count, id: \.self) { index in
                            Rectangle()
                                .fill(Color(realColours[index]))
                                .frame(minWidth: 50, minHeight: 300)
                        }
                    } // end of VStack
                    .padding()
                    .frame(maxWidth: .infinity)
                    
                    
                    Text(paletteString)
                        .padding()
                    
                    if !coloursFromUserPalette.isEmpty {
                        Divider()
                        
                        VStack {
                            Text("From Your Palette")
                                .font(.title2)
                                .bold()
                                .padding()
                            HStack(alignment: .center) {
                                ForEach(0..<coloursFromUserPalette.count, id: \.self) { index in
                                    Circle()
                                        .fill(Color(coloursFromUserPalette[index]))
                                        .frame(width: 30)
                                }
                            }
                            .padding()
                            Text(personalPaletteString)
                        } // end of VStack
                    }
                }
            }
                .disabled(true)
        }
    }
}


// MARK: Carousel Page
struct CarouselPage: View, Identifiable {
    var id: Int
    @ViewBuilder var content: any View
    
    var body: some View {
        ZStack {
            AnyView(content)
        }
        .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity, alignment: .center)
        .cornerRadius(20)
        .padding([.horizontal, .bottom], 20)
    }
}

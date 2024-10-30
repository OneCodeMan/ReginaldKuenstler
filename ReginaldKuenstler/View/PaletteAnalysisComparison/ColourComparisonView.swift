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
    @State var imgName = ""
    @State var infoString = ""
    @State var paletteString = ""
    @State var personalPaletteString = ""
    
    @State var realColours: [UIColor] = Array(repeating: .clear, count: 6)
    @State var estimatedColours: [UIColor] = Array(repeating: .clear, count: 6)
    @State var coloursFromUserPalette: [UIColor] = Array(repeating: .clear, count: 6)
    
    // MARK: Image states
    @State private var image = UIImage()
    @State private var showSheet = false
    @State private var showImagePicker = false
    @State private var sourceType: UIImagePickerController.SourceType = .photoLibrary
    
    @State var views: [CarouselPage] = []
    
    // MARK: Boolean view states
    @State private var disableScrollNoImageInput: Bool = true
    @State private var isImageSelected: Bool = false
    @State private var didImageSelectChange: Bool = false // Set to false after every image select. Disable Analyze if true. Set to true
    
    // Control current page index
    @State private var currentIndex = 0
    
    var body: some View {
        VStack {
            // TabView with Carousel Pages
            // can we disable tabview?
            TabView(selection: $currentIndex) {
                if !viewModel.isLoading {
                    CarouselPage(id: 0, content: {
                        ImageAnalysisInputView(currentTabViewIndex: $currentIndex,image: $image, showSheet: $showSheet, showImagePicker: $showImagePicker, sourceType: $sourceType, isImageSelected: $isImageSelected, didImageSelectChange: $didImageSelectChange, isLoading: $viewModel.isLoading, handleAnalyzePhoto: {
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
                }
                
                if isImageSelected {
                    CarouselPage(id: 1, content: {
                        PaletteResults(realColours: $realColours, paletteString: $paletteString, coloursFromUserPalette: $coloursFromUserPalette, personalPaletteString: $personalPaletteString, isLoading: $viewModel.isLoading, disableScrollNoImageInput: $disableScrollNoImageInput)
                    })
                    .tag(1)
                    .disabled(!isImageSelected) // Disable the second tab if no image is selected
                }
                
            }
            .tabViewStyle(PageTabViewStyle())
            .padding(.vertical, 20)
        }
        .toolbar(viewModel.isLoading ? .hidden : .visible, for: .tabBar)
        .onAppear {
            //            self.views = [
            //                CarouselPage(id: 0, content: {
            //                    ImageAnalysisInputView(image: $image, showSheet: $showSheet, showImagePicker: $showImagePicker, sourceType: $sourceType, isImageSelected: $isImageSelected, handleAnalyzePhoto: {
            //                        self.performColourAnalysis(onImage: self.image)
            //                    })
            //                }),
            //                CarouselPage(id: 1, content: {
            //                    PaletteResults(realColours: $realColours, paletteString: $paletteString, coloursFromUserPalette: $coloursFromUserPalette, personalPaletteString: $personalPaletteString, isLoading: $viewModel.isLoading, disableScrollNoImageInput: $disableScrollNoImageInput)
            //                })
            //            ]
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
                paletteString = String(paletteString.dropLast(2))
                
                // Update user palette
                if !relevantColoursFromUserPalette.isEmpty {
                    let minCount = min(relevantColoursFromUserPalette.count, coloursFromUserPalette.count)
                    for j in 0..<minCount {
                        coloursFromUserPalette[j] = relevantColoursFromUserPalette[j].uiColour
                        personalPaletteString += "\(relevantColoursFromUserPalette[j].name), "
                    }
                    personalPaletteString = String(personalPaletteString.dropLast(2))
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
    @Binding var currentTabViewIndex: Int
    @Binding var image: UIImage
    @Binding var showSheet: Bool
    @Binding var showImagePicker: Bool
    @Binding var sourceType: UIImagePickerController.SourceType
    @Binding var isImageSelected: Bool
    @Binding var didImageSelectChange: Bool
    @Binding var isLoading: Bool
    var handleAnalyzePhoto: () -> ()
    
    // MARK: State variables for alert
    @State private var displayAnalyzePressedNoImageInputAlert = false
    @State private var displayImageAlreadyAnalyzedAlert = false
    
    var body: some View {
        ZStack(alignment: .top) {
            VStack {
                Spacer()
                    .frame(height: 50)
                
                // Display the placeholder image if no image is selected
                if image.size.width == 0 && image.size.height == 0 {
                    Image(systemName: "photo.artframe")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .clipShape(RoundedRectangle(cornerRadius: 10))
                        .overlay(
                            Rectangle()
                                .stroke(Color.brownOuterFrameImage, lineWidth: 12)
                                .border(Color.goldInnerFrameImage, width: 14)
                        )
                        .padding()
                        .onTapGesture {
                            showSheet = true
                        }
                } else {
                    Image(uiImage: self.image)
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(minHeight: 400, maxHeight: 450)
                        .clipShape(RoundedRectangle(cornerRadius: 10))
                        .overlay(
                            Rectangle()
                                .stroke(Color.brownOuterFrameImage, lineWidth: 12)
                                .border(Color.goldInnerFrameImage, width: 14)
                        )
                        .edgesIgnoringSafeArea(.all)
                        .statusBar(hidden: true)
                        .padding()
                        .onTapGesture {
                            showSheet = true
                        }
                        // .redacted(reason: .placeholder)
                }
            }
            
            VStack {
                Text("Select photo")
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1)))
                    .cornerRadius(3)
                    .foregroundColor(.white)
                    .padding(.horizontal, 10)
                    .onTapGesture {
                        showSheet = true
                    }
                    .font(.defaultFontButton)
                
                Text("Analyze")
                    .font(.defaultFontButton)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(!isImageSelected ? Color.gray : Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1)))
                    .cornerRadius(3)
                    .foregroundColor(.white)
                    .padding(.horizontal, 10)
                    .onTapGesture {
                        if isImageSelected {
                            if didImageSelectChange {
                                print("Analyze button tapped, performing analysis on \(self.image)")
                                handleAnalyzePhoto()
                                didImageSelectChange = false
                            } else {
                                // we have an image, but the user already pressed Analyze on it and has not changed it.
                                displayImageAlreadyAnalyzedAlert = true // Show alert if no image is selected
                            }
                            
                        } else {
                            displayAnalyzePressedNoImageInputAlert = true // Show alert if no image is selected
                        }
                    }
                    // .disabled(!isImageSelected && !isLoading)
                    .opacity((!isImageSelected && !isLoading) ? 0.5 : 1)
                    .alert("Please select an image to analyze.", isPresented: $displayAnalyzePressedNoImageInputAlert) {
                        Button("OK") {}
                    }
                    .alert(isPresented: $displayImageAlreadyAnalyzedAlert) {
                        Alert(
                            title: Text("Image already analyzed"),
                            message: Text("This image has already been analyzed."),
                            dismissButton: .default(Text("OK"), action: {
                                withAnimation {
                                    currentTabViewIndex = 1
                                }
                            })
                        )
                    }
            }
            .padding()
            .frame(maxHeight: .infinity, alignment: .bottom)
        }
        .onChange(of: image) { newImage in
            isImageSelected = !(newImage.size.width == 0 && newImage.size.height == 0)
            didImageSelectChange = true
        }
        .actionSheet(isPresented: $showSheet) {
            ActionSheet(title: Text("Select Image"), message: Text("Please choose an option to select a photo"), buttons: [
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
    
    @State var showGridLoading: Bool = false
    var body: some View {
        if isLoading {
            VStack {
                if showGridLoading {
                    GridAnimationView()
                } else {
                    VStack {
                        Spacer()
                        ProgressView() {
                            Text("Loading")
                                .font(.defaultFontTitle)
                        }
                        .progressViewStyle(.circular)
                        Spacer()
                    }
                }
            }
            .onAppear {
                DispatchQueue.main.asyncAfter(deadline: .now() + 1.2) {
                    withAnimation {
                        showGridLoading.toggle()
                    }
                }
            }
        } else {
            ScrollView {
                VStack(alignment: .center) {
                    Spacer()
                        .frame(height: 30)
                    Text("Detected Colours")
                        .font(.defaultFontTitle)
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
                                .font(.defaultFontLargeTitle)
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

//
//  ColourComparisonView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import SwiftUI
import SwiftVibrantium

struct ColourComparisonView: View {
    @ObservedObject var viewModel = KuenstlerViewModel()
    @State var imgTitle = "Calum from Aftersun"
    @State var imgName = "starz"
    @State var infoString = "Title of Image"
    @State var paletteString = ""
    
    // real colours
    @State var realColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    // estimated colours
    @State var estimatedColours: [UIColor] = Array(repeating: .clear, count: 6)
    
    
    // image picker related
    @State private var image = UIImage(named: "beauty") ?? UIImage()
    @State private var showSheet = false
    @State private var showImagePicker = false
    @State private var sourceType: UIImagePickerController.SourceType = .photoLibrary
    // end of img picker related
    
    var body: some View {
        VStack {
            VStack(spacing: 0) {
//                Image(uiImage: UIImage(named: imgName)!)
//                    .resizable()
//                    .frame(width: 200, height: 200)
//                    .padding()
                
                Image(uiImage: self.image)
                    .resizable()
                    .scaledToFill()
                    .cornerRadius(50)
                    .frame(width: 300, height: 200)
                    .background(Color.black.opacity(0.2))
                    .aspectRatio(contentMode: .fill)
                    .clipShape(Rectangle())
                    .padding()
                
                Text("Change photo")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(LinearGradient(gradient: Gradient(colors: [Color(#colorLiteral(red: 0.262745098, green: 0.0862745098, blue: 0.8588235294, alpha: 1)), Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1))]), startPoint: .top, endPoint: .bottom))
                    .cornerRadius(16)
                    .foregroundColor(.white)
                    .padding(.horizontal, 20)
                    .onTapGesture {
                        showSheet = true
                    }
                
                Text("Analyze")
                    .font(.headline)
                    .frame(maxWidth: .infinity)
                    .frame(height: 50)
                    .background(LinearGradient(gradient: Gradient(colors: [Color(#colorLiteral(red: 0.262745098, green: 0.0862745098, blue: 0.8588235294, alpha: 1)), Color(#colorLiteral(red: 0.5647058824, green: 0.462745098, blue: 0.9058823529, alpha: 1))]), startPoint: .top, endPoint: .bottom))
                    .cornerRadius(16)
                    .foregroundColor(.white)
                    .padding(.horizontal, 20)
                    .onTapGesture {
                        print("Analyze button tapped, performing analysis on \(self.image)")
                        performColourAnalysis(onImage: self.image)
                    }
                
                Divider()
                
                // Results
                
                Text(infoString)
                    .padding()
                
                Divider()
                    .background(.white)
                    .frame(height: 2)
                
                // Real colours
                Text("Real Colours")
                HStack {
                    ForEach(0..<realColours.count, id: \.self) { index in
                        Rectangle()
                            .fill(Color(realColours[index]))
                            .frame(width: 20, height: 20)
                    }
                }
                .padding()
                
                // Estimated colours
                Divider()
                Text("Estimated Colours")
                VStack {
                    HStack {
                        ForEach(0..<estimatedColours.count, id: \.self) { index in
                            Rectangle()
                                .fill(Color(estimatedColours[index]))
                                .frame(width: 20, height: 20)
                        }
                    }
                    .padding()
                    Text(paletteString)
                }
                
                Divider()
                    .background(.white)
                    .frame(height: 2)
            }
            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity, alignment: .topLeading)
            .padding()
        }
        .padding(.horizontal, 20)
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
        .onAppear {
            performColourAnalysis(onImage: self.image)
        }
    }
    
    func performColourAnalysis(onImage img: UIImage) {
        // let image = UIImage(named: imgName)!
        
        // reset palette string
        paletteString = ""
        let artwork = Artwork(image: img, title: imgTitle)
        
        viewModel.performAnalOnImage(artwork: artwork) { colourPairs in
            DispatchQueue.main.async {
                // Loop through the colourPairs and assign to real and estimated colours
                for i in 0..<min(colourPairs.count, realColours.count) {
                    realColours[i] = colourPairs[i].actualColourInfo.uiColour
                    estimatedColours[i] = colourPairs[i].estimatedColourInfo.uiColour
                    paletteString += "\(colourPairs[i].name), "
                }
            }
        }
    }
}

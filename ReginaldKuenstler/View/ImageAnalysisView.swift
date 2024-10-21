//
//  ImageAnalysisView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

// https://designcode.io/swiftui-advanced-handbook-imagepicker/

import SwiftUI

struct ImageAnalysisView: View {
    @StateObject var viewModel = KuenstlerViewModel()
    @State private var image = UIImage(named: "beauty") ?? UIImage()
    @State private var showSheet = false
    @State private var showImagePicker = false
    @State private var sourceType: UIImagePickerController.SourceType = .photoLibrary
    
    var body: some View {
        HStack {
            Image(uiImage: self.image)
                .resizable()
                .cornerRadius(50)
                .frame(width: 100, height: 100)
                .background(Color.black.opacity(0.2))
                .aspectRatio(contentMode: .fill)
                .clipShape(Circle())
            
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
                    let artwork = Artwork(image: self.image, title: "")
                    viewModel.performAnalOnImage(artwork: artwork) { colourPairs, relevantColoursFromUserPalette in
                        print("colourPairs after analyze: \(colourPairs.count)")
                    }
                }
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
    }
}

#Preview {
    ImageAnalysisView()
}

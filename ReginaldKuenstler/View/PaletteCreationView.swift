//
//  PaletteCreationView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct PaletteColourSelectItem {
    let paletteColour: PaletteColour
    var isSelected: Bool
}

struct PaletteCreationView: View {
    @ObservedObject var viewModel: CreateUserPaletteViewModel = CreateUserPaletteViewModel()
    
    // Grid layout with 3 columns
    let columns = [
        GridItem(.flexible()),
        GridItem(.flexible()),
        GridItem(.flexible())
    ]
    
    var body: some View {
        VStack {
            // Display colours in a LazyVGrid
            LazyVGrid(columns: columns, spacing: 16) {
                ForEach(viewModel.paletteColours.indices, id: \.self) { index in
                    ColourCell(colour: $viewModel.paletteColours[index])
                        .onTapGesture {
                            viewModel.paletteColours[index].isSelected.toggle()
                        }
                }
            }
            .padding()
            
            // Button to save selected colours to UserDefaults
            Button(action: {
                viewModel.saveSelectedToUserDefaults()
            }) {
                Text("Save Selected Colours")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }
        }
    }
}

struct ColourCell: View {
    @Binding var colour: PaletteColourSelectItem
    
    var body: some View {
        ZStack {
            // Display the colour as a rectangle
            Rectangle()
                .fill(Color(colour.paletteColour.uiColour))
                .frame(height: 100)
                .cornerRadius(8)
            
            // Overlay with a checkmark if the colour is selected
            if colour.isSelected {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundColor(.white)
                    .font(.largeTitle)
                    .padding()
            }
        }
        .overlay(RoundedRectangle(cornerRadius: 8)
                    .stroke(colour.isSelected ? Color.blue : Color.clear, lineWidth: 4))
    }
}

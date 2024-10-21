//
//  ColourGridItem.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-21.
//

import SwiftUI

struct ColourGridItemView: View {
    @Binding var colourItem: PaletteColourSelectItem
    
    var body: some View {
        ZStack {
            // Display the colour as a rectangle
            VStack {
                Circle()
                    .stroke(.gray, lineWidth: 2)
                    .fill(Color(colourItem.paletteColour.uiColour))
                    .frame(height: 50)
                Text(colourItem.paletteColour.colourName)
                    .bold()
                    .foregroundStyle(colourItem.paletteColour.isUserOwned ? .gray : .black)
            }

            // OVERLAY with a checkmark if the colour is selected
            if colourItem.isSelected {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundColor(.white)
                    .font(.largeTitle)
            }
        }
        .overlay(RoundedRectangle(cornerRadius: 8)
        .stroke(colourItem.isSelected ? Color.blue : Color.clear, lineWidth: 4))
    }
}

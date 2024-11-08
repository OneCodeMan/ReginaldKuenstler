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
            VStack {
                Circle()
                    .stroke(.gray, lineWidth: 2)
                    .fill(Color(colourItem.paletteColour.uiColour))
                    .frame(height: 50)
                Text(colourItem.paletteColour.colourName)
                    .font(.defaultFontButton)
                    .bold()
                    .foregroundStyle(colourItem.paletteColour.isUserOwned ? .gray : .black)
                    .strikethrough(colourItem.paletteColour.isUserOwned)
            }
            .opacity(colourItem.paletteColour.isUserOwned ? 0.3 : 1.0)

            // OVERLAY with a checkmark if the colour is selected
            if colourItem.isSelected {
                Image(systemName: "checkmark.circle.fill")
                    .foregroundColor(.white)
                    .font(.largeTitle)
            }
        }
        .overlay(
            RoundedRectangle(cornerRadius: 8)
                .stroke(colourItem.isSelected ? Color.blue : Color.clear, lineWidth: 4)
                .background(colourItem.paletteColour.isUserOwned ? Color.gray.opacity(0.3) : Color.clear)
        )
    }
}

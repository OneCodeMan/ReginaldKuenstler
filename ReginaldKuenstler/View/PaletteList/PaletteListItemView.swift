//
//  PaletteListItemView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct PaletteListItemView: View {
    @State var paletteColourItem: PaletteColourSelectItem
    var body: some View {
        VStack {
            Circle()
                .stroke(.gray, lineWidth: 2)
                .fill(Color(paletteColourItem.paletteColour.uiColour))
                .frame(height: 50)
                .overlay(
                    Circle()
                        .stroke(paletteColourItem.isSelected ? Color.blue : Color.clear, lineWidth: 4) // Highlight if selected
                )
            Text(paletteColourItem.paletteColour.colourName)
                .bold()
                .strikethrough(paletteColourItem.paletteColour.isUserOwned)
                .foregroundStyle(paletteColourItem.paletteColour.isUserOwned ? .gray : .black)
                .font(.system(size: 14.0))
                .scaledToFill()
                .padding(.top, 3)
        }
        .padding()
        .opacity(paletteColourItem.paletteColour.isUserOwned ? 0.7 : 1.0)
    }
}

struct UserPaletteListItemView: View {
    @State var paletteColourItem: PaletteColour
    var body: some View {
        VStack {
            Circle()
                .stroke(.gray, lineWidth: 2)
                .fill(Color(paletteColourItem.uiColour))
                .frame(height: 50)
            Text(paletteColourItem.colourName)
                .bold()
                .font(.system(size: 14.0))
                .scaledToFill()
                .padding(.top, 3)
        }
        .padding()
        .opacity(paletteColourItem.isUserOwned ? 0.7 : 1.0)
    }
}

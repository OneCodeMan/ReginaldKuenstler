//
//  PaletteListItemView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct PaletteListItemView: View {
    @State var paletteColourItem: PaletteColour
    var body: some View {
        VStack {
            Circle()
                .stroke(.gray, lineWidth: 2)
                .fill(Color(paletteColourItem.uiColor))
                .frame(height: 50)
            Text(paletteColourItem.colourName)
                .bold()
                .foregroundStyle(paletteColourItem.isUserOwned ? .gray : .black)
        }
        .padding()
        .opacity(paletteColourItem.isUserOwned ? 0.7 : 1.0)
    }
}

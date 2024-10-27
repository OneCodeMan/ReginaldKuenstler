//
//  UserPalette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

import SwiftUI

struct UserPaletteView: View {
    @ObservedObject var userPaletteViewModel = UserPaletteViewModel()
    
    // MARK: search logic
    @State var searchText: String = ""
    
    // MARK: VGrid logic
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    // MARK: List edit mode
    @State private var isEditing: Bool = false
    @State private var isJiggling: Bool = false
    @State private var isPresentingConfirmation: Bool = false
    
    // MARK: Selected item for deletion
    @State private var itemToDelete: (paletteColour: PaletteColour, groupName: String)?
    
    var body: some View {
        NavigationStack {
            VStack {
                Text("")
                    .toolbar {
                        if isEditing {
                            Button("Done") {
                                withAnimation {
                                    isEditing.toggle()
                                }
                            }
                        } else {
                            NavigationLink(destination: PaletteCreationView()) {
                                Text("Add")
                            }
                        }
                    }
                
                // Keep search bar at the top level for consistency across states
                .searchable(text: $searchText)
                .onChange(of: searchText) { search in
                    if !search.isEmpty {
                        userPaletteViewModel.filterPaletteColours(term: search)
                    } else {
                        userPaletteViewModel.resetFilteredPaletteColours()
                    }
                }
                
                // State 1: User has no palette colors and is not searching
                if userPaletteViewModel.userPaletteColours.isEmpty && searchText.isEmpty {
                    Text("You have no colours.")
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                        .multilineTextAlignment(.center)
                
                // State 2: User is searching but there are no results for the search term
                } else if !userPaletteViewModel.userPaletteColours.isEmpty && !searchText.isEmpty && userPaletteViewModel.filteredUserPaletteColours.isEmpty {
                    Text("No results found for \"\(searchText)\".")
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                        .multilineTextAlignment(.center)
                
                // State 3: User is searching and there are results for the search term
                } else {
                    List {
                        ForEach(Array(userPaletteViewModel.groupedColours.keys), id: \.self) { groupName in
                            if let groupItems = userPaletteViewModel.groupedColours[groupName], !groupItems.isEmpty {
                                VStack(alignment: .leading) {
                                    Text(groupName)
                                        .font(.largeTitle)
                                        .bold()
                                        .padding([.top, .leading], 8)
                                    
                                    LazyVGrid(columns: self.columns) {
                                        ForEach(groupItems) { cI in
                                            UserPaletteListItemView(paletteColourItem: cI)
                                                .jiggle(isEnabled: self.isJiggling)
                                                .onTapGesture {
                                                    withAnimation {
                                                        if isEditing {
                                                            self.isPresentingConfirmation = true
                                                            self.itemToDelete = (cI, groupName)
                                                        }
                                                    }
                                                }
                                                .contentShape(Rectangle())
                                                .onLongPressGesture(minimumDuration: 0.2) {
                                                    withAnimation {
                                                        isEditing = true
                                                        isJiggling = true
                                                        delay(interval: 1.5) { self.isJiggling = false }
                                                    }
                                                }
                                                .overlay(
                                                    isEditing ? Button(action: {
                                                        self.isPresentingConfirmation = true
                                                        self.itemToDelete = (cI, groupName)
                                                    }) {
                                                        Image(systemName: "minus.circle.fill")
                                                            .foregroundColor(.red)
                                                    }
                                                    .padding(8) : nil,
                                                    alignment: .topTrailing
                                                )
                                        }
                                    }
                                    .listRowSeparator(.hidden)
                                    .padding()
                                }
                                .listRowSeparator(.hidden)
                            }
                        }
                    }
                }
            }
            .navigationTitle("Your Palette")
            .onAppear {
                self.userPaletteViewModel.fetchUserPalettes()
            }
            .alert("Are you sure you want to delete this colour?", isPresented: $isPresentingConfirmation) {
                Button("Delete", role: .destructive) {
                    if let item = itemToDelete {
                        withAnimation(.easeOut) {
                            userPaletteViewModel.deletePaletteColourFromUserPalette(paletteColour: item.paletteColour, groupName: item.groupName)
                        }
                    }
                }
                Button("Cancel", role: .cancel) {
                    isPresentingConfirmation = false
                }
            }
        }
    }
}


#Preview {
    UserPaletteView()
}

func delay(interval: TimeInterval, closure: @escaping () -> Void) {
    DispatchQueue.main.asyncAfter(deadline: .now() + interval, execute: closure)
}
